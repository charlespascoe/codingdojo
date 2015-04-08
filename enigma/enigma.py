import string
import sys
import json

alph = string.ascii_uppercase


class InvalidLetterException(Exception):
    pass


class Rotor:
    def __init__(self, wiring, rollover=None, disp=None, ring_pos=1):
        self.mapping = [alph.index(letter) for letter in wiring]
        self.next_rotor = None
        self.prev_rotor = None
        self.disp = alph.index(disp) if disp is not None else 0
        self.rollover = alph.index(rollover) if rollover is not None else None

        ring_pos -= 1

        self.disp += (len(alph) - ring_pos) % len(alph)
        if self.rollover:
            self.rollover += (len(alph) - ring_pos) % len(alph)

    def increment(self):
        # if the next rotor is a rotor (and not a reflector)
        # and this rotor's notch (rollover) is aligned with a pawl,
        # then rotate (i.e. the second step in a doublestep), or rotate if previous notch is aligned
        if (self.next_rotor.increment() and self.notch_aligned()) or self.prev_rotor.notch_aligned():
            self.disp = self.rotate(1)

        return True

    def encode(self, val):
        self.next_rotor.encode(self.rotate(self.mapping[self.rotate(val)], True))

    def reflect(self, val):
        self.prev_rotor.reflect(self.rotate(self.mapping.index(self.rotate(val)), True))

    def notch_aligned(self):
        return self.disp == self.rollover

    def rotate(self, val, subtract=False):
        return (val + ((len(alph) - self.disp) if subtract else self.disp)) % len(alph)


class Reflector(Rotor):
    def __init__(self, wiring):
        super().__init__(wiring)

    def increment(self):
        return False

    def encode(self, val):
        self.prev_rotor.reflect(self.mapping[val])


class EntryRotor(Rotor):
    def __init__(self):
        self.next_rotor = None

    def increment(self):
        self.next_rotor.increment()

    def encode(self, val):
        self.next_rotor.encode(val)

    def reflect(self, val):
        self.result = val

    def notch_aligned(self):
        return True


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
        self.plugboard = plugboard

        self.entry_rotor = EntryRotor()
        prev_rotor = self.entry_rotor

        for rotor in rotors:
            prev_rotor.next_rotor = rotor
            rotor.prev_rotor = prev_rotor
            prev_rotor = rotor

        prev_rotor.next_rotor = reflector
        reflector.prev_rotor = prev_rotor

    def encode(self, letter):
        if letter not in alph:
            raise InvalidLetterException()

        val = alph.index(letter)

        self.entry_rotor.increment()
        self.entry_rotor.encode(self.plugboard.encode(val))

        return alph[self.plugboard.encode(self.entry_rotor.result)]


if __name__ == '__main__':
    args = sys.argv[1:]

    plugboard = None
    rotors = []
    reflector = None

    if len(args) == 0:
        sys.stderr.write('No setup file provided, defaulting to I-II-III, MCK, Reflector B\n')

        plugboard = Plugboard([])

        # Rotor III
        rotors.append(Rotor('BDFHJLCPRTXVZNYEIWGAKMUSQO', 'V', 'K'))

        # Rotor II
        rotors.append(Rotor('AJDKSIRUXBLHWTMCQGZNPYFVOE', 'E', 'C'))

        # Rotor I
        rotors.append(Rotor('EKMFLGDQVZNTOWYHXUSPAIBRCJ', 'Q', 'M'))

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

    for letter in sys.stdin.read():
        letter = letter.upper()
        if letter in alph:
            output_str += engima.encode(letter)

    sys.stdout.write(output_str)
    sys.stdout.close()

    # Adds newline, looks better when stdout is terminal
    sys.stderr.write('\n')
