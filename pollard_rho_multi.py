from fractions import gcd
import argparse

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
    if d == n:
        print(n)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pollard-Rho Primality Testing')
    parser.add_argument('n', type=int, help='number to which to test up')
    args = parser.parse_args()
    n = args.n

    jobs = []
    for n in range(2,n):
        pollard_rho(n)

