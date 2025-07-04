# Following Jantzen Lee's tutorial
# https://www.youtube.com/watch?v=EHYEQM1sA3o&list=PLaBr_WzeIAixidGwqfcrQlwKZX4RZ2E7D

import numpy as np

# Episode 1
def episode_one():
    # He mentions the lorentz force formula, and I had chat gpt make a random example using it
    # Given constants
    q = 1.6e-19  # charge in Coulombs

    # Vectors (velocity in m/s, electric field in V/m, magnetic field in Tesla)
    v = np.array([2e6, 3e6, 0])
    E = np.array([0, 0, 5e3])
    B = np.array([0, 0, 2])

    # Lorentz force calculation: F = q * (E + v x B)
    v_cross_B = np.cross(v, B)
    F = q * (E + v_cross_B)

    # v × B = [ 6000000. -4000000.        0.]
    # Lorentz Force F = [ 9.6e-13 -6.4e-13  8.0e-16] N
    print("v × B =", v_cross_B)
    print("Lorentz Force F =", F, "N")



episode_one()
