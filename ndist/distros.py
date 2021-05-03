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
        return self.SAMPLER(*self.args, **self.kwargs, size=shape)

    def _arith(self, op, other):
        dist = Distro()
        if isinstance(other, Distro):
            dist.SAMPLER = lambda size: op(self.sample(size), other.sample(size))
        else:
            dist.SAMPLER = lambda size: op(self.sample(size), other)
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


class Joint(Distro):
    """
    Joint distribution.
    """

    def __init__(self, distros):
        self.SAMPLER = distros

    def sample(self, shape):
        return np.stack([dist.sample(shape) for dist in self.SAMPLER], axis=0)


class Normal(Distro):
    SAMPLER = np.random.normal

class Uniform(Distro):
    SAMPLER = np.random.uniform

class Power(Distro):
    SAMPLER = np.random.power

class Pareto(Distro):
    SAMPLER = np.random.pareto

class Poisson(Distro):
    SAMPLER = np.random.poisson

class Sample(Distro):
    SAMPLER = np.random.sample
