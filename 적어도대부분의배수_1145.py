import sys
import itertools
num = list(map(int, sys.stdin.readline().strip().split()))
num.sort()


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


m = num[-1] * num[-2] * num[-3]
for comb in itertools.combinations(num, 3):
    a, b, c = comb[0], comb[1], comb[2]
    d = a * b // gcd(a, b)
    e = c * d // gcd(c, d)
    m = min(m, e)
print(m)