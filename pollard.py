from fractions import gcd

n = 786
B = 1000

a = 2
for j in range(2, B):
    print(a)
    a = pow(a, j) % n
d = gcd(a-1, n)

if d < n and d > 1:
    print("{d} is a factor of {n}".format(d=d, n=n))
else:
    print("no factor of {n} is found".format(n=n))
