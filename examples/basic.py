"""
Basic usage example.
"""
from ndist import distros


if __name__ == '__main__':
    dist = distros.Normal(loc=100, scale=10)
    samples = dist.sample((5, 5))
    print("\nNormal(100, 10)")
    print(samples)
    print(samples.mean(), samples.std())

    dist = distros.Uniform(low=0, high=100)
    samples = dist.sample((5, 5))
    print("\nUniform(0, 100)")
    print(samples)
    print(samples.min(), samples.max())

    dist = distros.Power(a=8)
    samples = dist.sample((5, 5))
    print("\nPower(8)")
    print(samples)
    print(samples.mean(), samples.std())
