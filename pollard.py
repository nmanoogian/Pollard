from fractions import gcd
import argparse

def pollard(n, B, a):
    for j in range(2, B):
        print(a)
        a = pow(a, j) % n
    d = gcd(a-1, n)

    if d < n and d > 1:
        return d
    else:
        return None


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Pollard Factorization Algorithm.')
    parser.add_argument('n', type=int, help='number to test')
    parser.add_argument('B', type=int, help='a large number to use for factorization')
    parser.add_argument('a', type=int, help='a number to use for exponentiation')
    args = parser.parse_args()

    n = args.n
    B = args.B

    d = pollard(n, B, args.a)
    if d:
        print("{d} is a factor of {n}".format(d=d, n=n))
    else:
        print("no factor of {n} is found".format(n=n))
