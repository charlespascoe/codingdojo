import string
alph = string.ascii_uppercase


class InvalidLetterException(Exception):
    pass


class Rotor:
    def __init__(self, setup_string, rollover=None, disp=None):
        self.mapping = [alph.index(letter) for letter in setup_string]
        self.next_rotor = None
        self.prev_roto = None
        self.disp = alph.index(disp) if disp is not None else 0
        self.rollover = alph.index(rollover) if rollover is not None else None

    def increment(self):
        if self.disp == self.rollover:
            self.next_rotor.increment()
        self.disp = (self.disp + 1) % len(alph)

    def encode(self, val):
        self.next_rotor.encode(self.rotate(self.mapping[self.rotate(val)]))

    def reflect(self, val):
        self.prev_rotor.reflect(self.rotate(self.mapping.index(self.rotate(val))))

    def rotate(self, val):
        return (val + self.disp) % len(alph)


class Reflector(Rotor):
    def __init__(self, setup_string):
        super().__init__(setup_string)

    def increment(self):
        pass

    def encode(self, val):
        self.prev_rotor.reflect(self.mapping[val])


class Plugboard:
    def __init__(self, mapping):
        self.mapping = [0 for i in range(len(alph))]

        for pair in mapping:
            a, b = pair
            mapping[a] = b
            mapping[b] = a

    def encode(self, val):
        return self.mapping[val]


class EnigmaMachine:
    def __init__(self, rotors, reflector, plugboard):
        self.next_rotor = None
        prev_rotor = self

        for rotor in rotors:
            prev_rotor.next_rotor = rotor
            rotor.prev_rotor = prev_rotor
            prev_rotor = rotor

        prev_rotor.next_rotor = reflector
        reflector.prev_rotor = prev_rotor

        self.plugboard = plugboard

        self.output = None

    def encode(self, letter):
        if letter not in alph:
            raise InvalidLetterException()

        val = alph.index(letter)

        self.next_rotor.increment()
        self.next_rotor.encode(self.plugboard.encode(val))


    def reflect(self, val):
        result = self.plugboard.encode(val)

        if self.output:
            self.output(alph[result])

