"""
Distribution definition.
"""
import numpy as np


class Distro:
    """
    Distribution data structure.
    """

    SAMPLER = None

    def __init__(self, *a, **kw):
        self.args = a
        self.kwargs = kw

    def sample(self, shape):
        try:
            return self.SAMPLER(*self.args, **self.kwargs, shape=shape)
        except TypeError:
            return self.SAMPLER(*self.args, **self.kwargs, size=shape)



class Normal(Distro):
    SAMPLER = np.random.normal


class Uniform(Distro):
    SAMPLER = np.random.uniform


class Power(Distro):
    SAMPLER = np.random.power
