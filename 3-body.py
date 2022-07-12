import numpy as np
import scipy as sp

from scipy import constants

class oneBody:
    def __init__(self, mass):
        self.mass = mass

    def gravitational_field(x, y):
        modulus = np.sqrt(x**2 + y**2)
        g = -sp.constants.physical_constants[G]*self.mass/modulus**2*[x/modulus, y/modulus]
        return g