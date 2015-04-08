import unittest
import enigma
import json


def add_tests(suite, cls, data=None):
    for func in dir(cls):
        if func.startswith('test'):
            suite.addTest(cls(func, data))


class TestCase(unittest.TestCase):
    def __init__(self, methodname='', data=None):
        super().__init__(methodname)
        self.data = data

    # Make method names PEP8 compliant
    def setUp(self):
        self.setup()

    def setup(self):
        pass

    def tearDown(self):
        self.teardown()

    def teardown(self):
        pass


class TestingRotor(enigma.Rotor):
    def __init__(self):
        self.is_notch_aligned = False
        self.is_reflector = False

    def encode(self, val):
        self.encode_result = val

    def reflect(self, val):
        self.reflect_result = val

    def increment(self):
        return not self.is_reflector

    def notch_aligned(self):
        return self.is_notch_aligned


class RotorTests(TestCase):
    def setup(self):
        self.rotor = enigma.Rotor(self.data['wiring'], self.data['rollover'])
        self.dummy_rotor = TestingRotor()
        self.rotor.next_rotor = self.dummy_rotor
        self.rotor.prev_rotor = self.dummy_rotor

    def test_mapping(self):
        for subtest in self.data['tests']['mapping']:
            with self.subTest(subtest=subtest):
                self.rotor.disp = enigma.alph.index(subtest['disp'])
                input_val = enigma.alph.index(subtest['input'])
                expected_val = enigma.alph.index(subtest['output'])

                self.rotor.encode(input_val)
                self.assertEqual(self.dummy_rotor.encode_result, expected_val)

    def test_reflect(self):
        for subtest in self.data['tests']['mapping']:
            with self.subTest(subtest=subtest):
                self.rotor.disp = enigma.alph.index(subtest['disp'])
                input_val = enigma.alph.index(subtest['input'])
                output_val = enigma.alph.index(subtest['output'])

                self.rotor.reflect(output_val)
                self.assertEqual(self.dummy_rotor.reflect_result, input_val)

    def test_increment(self):
        # Rotor should only increment if the previous rotor
        # it in the rollover position

        self.dummy_rotor.is_notch_aligned = False
        self.rotor.disp = 10

        self.rotor.increment()

        self.assertEqual(self.rotor.disp, 10)

        self.dummy_rotor.is_notch_aligned = True
        self.rotor.increment()

        self.assertEqual(self.rotor.disp, 11)

    def test_doublestep(self):
        self.dummy_rotor.is_notch_aligned = False
        self.dummy_rotor.is_reflector = True
        self.rotor.disp = self.rotor.rollover

        self.rotor.increment()

        # No change if the next rotor is a reflector
        self.assertEqual(self.rotor.disp, self.rotor.rollover)

        self.dummy_rotor.is_reflector = False

        self.rotor.disp = 0

        self.rotor.increment()

        # No change if the next rotor is not a reflector
        # and the rotor is not in the rollover position
        # (assuming non-zero rollover position)
        self.assertEqual(self.rotor.disp, 0)

        self.rotor.disp = self.rotor.rollover

        self.rotor.increment()

        # Increment if next rotor is not relfector and in rollover position
        self.assertEqual(self.rotor.disp, (self.rotor.rollover + 1) % len(enigma.alph))

    def teardown(self):
        del self.rotor
        del self.dummy_rotor


class ReflectorTests(TestCase):
    def setup(self):
        self.reflector = enigma.Reflector(self.data['wiring'])
        self.dummy_rotor = TestingRotor()
        self.reflector.prev_rotor = self.dummy_rotor

    def test_mapping(self):
        for subtest in self.data['tests']['mapping']:
            with self.subTest(subtest=subtest):
                input_val = enigma.alph.index(subtest['input'])
                output_val = enigma.alph.index(subtest['output'])

                self.reflector.encode(input_val)

                self.assertEqual(self.dummy_rotor.reflect_result, output_val)

    def teardown(self):
        del self.reflector
        del self.dummy_rotor


class PlugboardTests(TestCase):
    def test_mapping(self):
        pass


class EnigmaTests(TestCase):
    def setup(self):
        plugboard = enigma.Plugboard(self.data['plugboard'])
        rotors = [enigma.Rotor(r['wiring'], r['rollover'], r['disp']) for r in self.data['rotors']]
        reflector = enigma.Reflector(self.data['reflector'])

        self.enigma = enigma.EnigmaMachine(plugboard, rotors, reflector)

    def test_encryption(self):
        for subtest in self.data['tests']:
            self.setup()
            with self.subTest(subTest=subtest):
                plaintext = subtest['plaintext']
                expected_ciphertext = subtest['ciphertext']

                ciphertext = ''

                for letter in plaintext:
                    ciphertext += self.enigma.encode(letter)

                self.assertEqual(ciphertext, expected_ciphertext)

    def test_decryption(self):
        for subtest in self.data['tests']:
            self.setup()
            with self.subTest(subtest=subtest):
                expected_plaintext = subtest['plaintext']
                ciphertext = subtest['ciphertext']

                plaintext = ''

                for letter in ciphertext:
                    plaintext += self.enigma.encode(letter)

                self.assertEqual(plaintext, expected_plaintext)

    def teardown(self):
        del self.enigma


if __name__ == '__main__':
    with open('testing.json') as f:
        test_data = json.loads(f.read())['test_cases']

    suite = unittest.TestSuite()

    for rotor_test_data in test_data['rotor']:
        add_tests(suite, RotorTests, rotor_test_data)

    for reflector_test_data in test_data['reflector']:
        add_tests(suite, ReflectorTests, reflector_test_data)

    add_tests(suite, PlugboardTests)

    for enigma_test_data in test_data['enigma']:
        add_tests(suite, EnigmaTests, enigma_test_data)

    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
