import numpy as np
import scipy as sp

from scipy import constants

class oneBody:
    def __init__(self, mass):
        self.mass = mass

    def gravitational_field(self, x, y):
        modulus = np.sqrt(x**2 + y**2)
        g_x = -constants.G*self.mass/(modulus**2)*x/modulus
        g_y = -constants.G*self.mass/(modulus**2)*y/modulus
        g = [g_x, g_y]
        return g

    def get_mass(self):
        return self.mass

