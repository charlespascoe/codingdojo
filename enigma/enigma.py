import string
alph = string.ascii_uppercase

class Rotor:
    def __init__(self, setup_string, rollover):
        self.mapping = [alph.index(letter) for letter in setup_String]
        self.next_rotor = None
        self.prev_roto = None
        self.disp = 0
        self.rollover = alph.index(rollover)
        
        
