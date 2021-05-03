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

    def _arith(self, op, other):
        dist = Distro()
        dist.SAMPLER = lambda shape: op(self.sample(shape), other)
        return dist

    def __add__(self, other):
        return self._arith(lambda a, b: a + b, other)

    def __iadd__(self, other):
        return self + other

    def __sub__(self, other):
        return self._arith(lambda a, b: a - b, other)

    def __isub__(self, other):
        return self - other

    def __mul__(self, other):
        return self._arith(lambda a, b: a * b, other)

    def __imul__(self, other):
        return self * other

    def __div__(self, other):
        return self._arith(lambda a, b: a / b, other)
    
    def __idiv__(self, other):
        return self / other


class Normal(Distro):
    SAMPLER = np.random.normal


class Uniform(Distro):
    SAMPLER = np.random.uniform


class Power(Distro):
    SAMPLER = np.random.power
