# Documentation

## 1 - Rotors
### 1.1 - Rotor displacement

In enigma.py, the Rotor.encode adds the displacement to the value, and then subtracts the displacement to the mapped result. The addition because the the position of 'A' on the rotor has advanced that many letters, so the value going into the rotor needs to be adjusted. The subtraction is because the output letter has also advanced, so that needs to be adjusted before going to the next rotor. Here's an example of this:

- Imagine a rotor sandwiched between two fixed plates; on each plate there are 26 electrical contacts, 0 to 25, starting with 0 at the top (so initially, the letter ‘A’ on the rotor will line up with contact 0 on both plates, ‘B’ with 1, and so on)
- If the rotor is shifted one place forward, the letter ‘B’ would line up with 0 (‘C’ with 1, ‘A’ with 25, etc.). If a voltage is applied to contact 0, it is applied to ‘B’, which in the code is the same as taking the contact value (0) and adding the rotor displacement (1), and getting the mapped value
- Let’s say, for the sake of example, that ‘B’ maps to ‘C’. Since the rotor has been rotated, ‘C’ (which initially lined up with contact 2) now lines up with contact 1. This is replicated in the code by the subtraction after the mapping.


