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
        self.disp = (self.disp + 1) % len(alph)
        # Check rollover
    
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
    pass


class EnigmaMachine:
    def __init__(self, *rotors):
        self.next_rotor = None
        prev_rotor = self
        for rotor in rotors:
            prev_rotor.next_rotor = rotor
            rotor.prev_rotor = prev_rotor
            prev_rotor = rotor
    
    def reflect(self, val):
        
        
    