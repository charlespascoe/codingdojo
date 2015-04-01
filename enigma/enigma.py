import string
alph = string.ascii_uppercase


class Rotor:
    def __init__(self, setup_string, rollover, disp=0):
        self.mapping = [alph.index(letter) for letter in setup_String]
        self.next_rotor = None
        self.prev_roto = None
        self.disp = disp
        self.rollover = alph.index(rollover)

    def increment(self):
        if self.disp == self.rollover:
            self.next_rotor.increment()
        self.disp = (self.disp + 1) % len(alph)

    def encode(self, val):
        self.next_rotor.encode(self.mapping[val])

    def reflect(self, val):
        self.prev_rotor.reflect(self.mapping.index(val))


class Reflector(Rotor):
    def increment(self):
        pass

    def encode(self, val):
        self.prev_rotor(self.mapping[val])


class Plugboard:
    def __init__(self, mapping):
        self.mapping = [0 for i in range(len(alph))]

        for pair in mapping:
            a, b = pair
            mapping[a] = b
            mapping[b] = a

    def encode(self, val):



class EnigmaMachine:
    def __init__(self, *rotors):
        self.next_rotor = None
        prev_rotor = self
        for rotor in rotors:
            prev_rotor.next_rotor = rotor
            rotor.prev_rotor = prev_rotor
            prev_rotor = rotor

    def reflect(self, val):
        pass
