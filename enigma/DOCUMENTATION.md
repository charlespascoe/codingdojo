# Documentation

## 1 - Rotors
### 1.1 - Rotor displacement

In enigma.py, the Rotor.encode adds the displacement to the value, and then adds the displacement to the mapped result. The first addition because the the position of 'A' on the rotor has advanced that many letters, so the value going into the rotor needs to be adjusted. The second addition is because the output letter has also advanced, so that needs to be adjusted before going to the next rotor.

Example:

- The rotor has advanced 1 place, so that 'B' is at the top (and so 'A' from the plugboard goes into 'B' on the rotor); this is 1 more than 'A', so 1 must be added
- Let's say that this maps to 'Q'; 'Q' has advanced by 1 position, so 'Q' now lines up with 'R' on the next rotor (assuming the next rotor has no displacement)
- This transformation is independant of position of the rotors either side of it, as the calculations always give the value relative to 'A'


