import string
import sys
import json

alph = string.ascii_uppercase


class InvalidLetterException(Exception):
    pass


class Rotor:
    def __init__(self, wiring, rollover=None, disp=None):
        self.mapping = [alph.index(letter) for letter in wiring]
        self.next_rotor = None
        self.prev_roto = None
        self.disp = alph.index(disp) if disp is not None else 0
        self.rollover = alph.index(rollover) if rollover is not None else None

    def increment(self):
        if self.disp == self.rollover:
            self.next_rotor.increment()
        self.disp = (self.disp + 1) % len(alph)

    def encode(self, val):
        self.next_rotor.encode(self.rotate(self.mapping[self.rotate(val)], True))

    def reflect(self, val):
        self.prev_rotor.reflect(self.rotate(self.mapping.index(self.rotate(val)), True))

    def rotate(self, val, subtract=False):
        return (val + ((len(alph) - self.disp) if subtract else self.disp)) % len(alph)


class Reflector(Rotor):
    def __init__(self, wiring):
        super().__init__(wiring)

    def increment(self):
        pass

    def encode(self, val):
        self.prev_rotor.reflect(self.mapping[val])


class Plugboard:
    def __init__(self, mapping):
        self.mapping = [i for i in range(len(alph))]

        for pair in mapping:
            a, b = pair

            if a not in alph or b not in alph:
                raise InvalidLetterException()

            a = alph.index(a)
            b = alph.index(b)

            self.mapping[a] = b
            self.mapping[b] = a

    def encode(self, val):
        return self.mapping[val]


class EnigmaMachine:
    def __init__(self, plugboard, rotors, reflector):
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


if __name__ == '__main__':
    args = sys.argv[1:]

    plugboard = None
    rotors = []
    reflector = None

    if len(args) == 0:
        sys.stderr.write('No setup file provided, defaulting to I-II-III, MCK, Reflector B\n')

        plugboard = Plugboard([])

        # Rotor III
        rotors.append(Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V', 'M'))

        # Rotor II
        rotors.append(Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E', 'C'))

        # Rotor I
        rotors.append(Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q', 'K'))

        reflector = Reflector('YRUHQSLDPXNGOKMIEBFZCWVJAT')
    else:
        with open(args[0]) as f:
            data = json.loads(f.read())

        plugboard = Plugboard(data['plugboard'])

        for rotor in data['rotors']:
            rotors.append(Rotor(**rotor))

        reflector = Reflector(data['reflector'])

    engima = EnigmaMachine(plugboard, rotors, reflector)

    output_str = ''

    def output(letter):
        global output_str
        output_str += letter

    engima.output = output

    for letter in sys.stdin.read():
        letter = letter.upper()
        if letter in alph:
            engima.encode(letter)

    sys.stdout.write(output_str)
    sys.stdout.close()

    # Adds newline, looks better when stdout is terminal
    sys.stderr.write('\n')
