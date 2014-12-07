from fractions import gcd
import argparse
import multiprocessing as mp

class Number():
    """
    Represents a number and a single factor
    """
    def __init__(self, value, factor):
        self.value = value
        self.factor = factor

    def is_prime(self):
        return self.factor == self.value

    def __repr__(self):
        if self.is_prime():
            return "{v} is prime".format(v=self.value)
        else:
            return "{v}={f}*{x}".format(v=self.value, f=self.factor, x=(self.value//self.factor))

def pollard_rho(n, g=lambda x, n: (x**2 + 1) % n):
    """
    Runs the Pollard-Rho Algorithm
    The default g function: g(x, n) = (x^2 + 1) mod n
    """
    n_length = len(str(n)) + 1
    x = 2
    y = 2
    d = 1
    while d == 1:
        x = g(x, n)
        y = g(g(y, n), n)
        d = gcd(abs(x-y), n)
    return Number(n, d)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pollard-Rho Primality Testing')
    parser.add_argument('n', type=int, help='number to which to test up')
    args = parser.parse_args()
    n = args.n

    pool = mp.Pool()
    for x in pool.map(pollard_rho, range(2, n)):
        print(x)
