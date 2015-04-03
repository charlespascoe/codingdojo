import unittest
import enigma
import json


rotor_1 = enigma.Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
rotor_2 = enigma.Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
rotor_3 = enigma.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
reflector = enigma.Reflector('QYHOGNECVPUZTFDJAXWMKISRBL')


def add_tests(suite, cls, data=None):
    for func in dir(cls):
        if func.startswith('test'):
            suite.addTest(cls(func, data))

class TestCase(unittest.TestCase):
    def __init__(self, methodName='', data=None):
        super().__init__(methodName)
        self.data = data


class TestingRotor(enigma.Rotor):
    def __init__(self):
        self.incremented = False

    def encode(self, val):
        self.encode_result = val

    def reflect(self, val):
        self.reflect_result = val

    def increment(self):
        self.incremented = True

class RotorTests(TestCase):
    def setUp(self):
        self.rotor = enigma.Rotor(self.data['setup_string'], self.data['rollover'])
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

    def test_increment(self):
        # Rotor should only increment the next rotor if
        # it is leaving the rollover position

        self.rotor.disp = self.rotor.rollover - 1
        self.rotor.increment()
        # Now on the rollover position, no increment
        self.assertFalse(self.dummy_rotor.incremented)
        self.rotor.increment()
        # Should have incremented next rotor
        self.assertTrue(self.dummy_rotor.incremented)


class ReflectorTests(TestCase):
    def setUp(self):
        self.reflector = enigma.Reflector(self.data['setup_string'])
        self.dummy_rotor = TestingRotor()
        self.reflector.prev_rotor = self.dummy_rotor

    def test_mapping(self):
        for subtest in self.data['tests']['mapping']:
            with self.subTest(subtest=subtest):
                input_val = enigma.alph.index(subtest['input'])
                output_val = enigma.alph.index(subtest['output'])

                self.reflector.encode(input_val)

                self.assertEqual(self.dummy_rotor.reflect_result, output_val)

class PlugboardTests(TestCase):
    def test_mapping(self):
        pass


if __name__ == '__main__':
    with open('testing.json') as f:
        test_data = json.loads(f.read())['test_cases']

    suite = unittest.TestSuite()
    add_tests(suite, RotorTests, test_data['rotors']['I'])
    add_tests(suite, ReflectorTests, test_data['reflector'])
    add_tests(suite, PlugboardTests)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)

