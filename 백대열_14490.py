import sys


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


case = sys.stdin.readline().strip().split(':')
a, b = int(case[0]), int(case[1])
a, b = a // gcd(a, b), b // gcd(a, b)
print(f'{a}:{b}')