import unittest
import enigma



rotor_1 = enigma.Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
rotor_2 = enigma.Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E')
rotor_3 = enigma.Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V')
reflector = enigma.Reflector('QYHOGNECVPUZTFDJAXWMKISRBL')


class TestingRotor(enigma.Rotor):
    def __init__(self):
        pass

    def encode(self, val):
        self.encode_result = val

    def reflect(self, val):
        self.reflect_result = val


class RotorTesting(unittest.TestCase):
    def setUp(self):
        self.rotor = enigma.Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q')
        self.dummy_rotor = TestingRotor()
        self.rotor.next_rotor = self.dummy_rotor
        self.rotor.prev_rotor = self.dummy_rotor

    def test_initial_mapping(self):
        self.rotor.encode(enigma.alph.index('D'))
        self.assertEqual(self.dummy_rotor.encode_result, enigma.alph.index('F'))

    def test_displaced_mapping(self):
        self.rotor.disp = 5
        self.rotor.encode(enigma.alph.index('K'))
        # K = 10, 10 + 5 = 15, 15 (rotor)=> 7, 7 + 5 = 12, 12 (alph)=> M
        # See section 1.1 in the documentation
        self.assertEqual(self.dummy_rotor.encode_result, enigma.alph.index('M'))
        # TODO: add more advanced stuff, such as modulo is used


if __name__ == '__main__':
    unittest.main()

