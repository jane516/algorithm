import sys


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    return gcd(b, a % b)


def e_gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return [a, 1, 0]
    else:
        x1, x2 = 1, 0
        y1, y2 = 0, 1
        while b > 0:
            q = a // b
            r = a - q * b
            x = x1 - q * x2
            y = y1 - q * y2
            a, b = b, r
            x1, x2 = x2, x
            y1, y2 = y2, y
        return [a, x1, y1]


case = sys.stdin.readline().strip()
N = int(case.split()[0])
A = int(case.split()[1])
if gcd(A, N) != 1:
    print(N - A, -1)
else:
    print(N - A, e_gcd(A, N)[2] % N)