"""
Demonstrate law of large number on thin and fat tailed distribution.
Over time as we sample more and more values from a distribution, the
mean and standard deviation of a gaussian(thin tail) will converge.
On the other hand, fat tailed distributions may not ever or will
take a very large number of samples to converge.

Based on N.N. Taleb's video: https://www.youtube.com/watch?v=zyBXNIskQK0
"""
import matplotlib.pyplot as plt
from ndist import distros


def plot(distro, ax, title="", n=10**5):
    N = list(range(2, n))
    samples = distro(max(N))
    STD = [samples[:n].std() for n in N]
    ax.plot(N, STD)
    ax.set_title(title)


if __name__ == '__main__':
    fig, axs = plt.subplots(2, 1)
    plot(distros.Normal(0, 1), axs[0], "Thin Tailed(Gaussian)")
    plot(distros.Cauchy(), axs[1], "Fat Tailed(Cauchy)")
    plt.show()
