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
        print("x={x} y={y} d={d}".format(x=str(x).ljust(n_length), y=str(y).ljust(n_length), d=str(d).ljust(n_length)))
        iterations += 1
    if d == n:
        return None
    else:
        return d


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pollard-Rho Factorization Algorithm.')
    parser.add_argument('n', type=int, help='number to test')
    args = parser.parse_args()

    n = args.n

    print("Pollard-Rho: g(x) = x^2 + 1")
    d = pollard_rho(n)
    if d:
        print("{d} is a factor of {n}".format(d=d, n=n))
    else:
        print("no factor of {n} is found".format(n=n))

    print("\nPollard-Rho: g(x) = x^2 - 1")
    d = pollard_rho(n, g=lambda x, n: (x**2 - 1) % n)
    if d:
        print("{d} is a factor of {n}".format(d=d, n=n))
    else:
        print("no factor of {n} is found".format(n=n))

