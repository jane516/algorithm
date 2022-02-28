import sys


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


T = int(sys.stdin.readline().strip())
for i in range(T):
    case = sys.stdin.readline().strip().split()
    a, b = int(case[0]), int(case[1])
    while True:
        if a == 1:
            print(b)
            break
        c = b // a + 1
        a = a * c - b
        b = b * c
        a, b = a // gcd(a, b), b // gcd(a, b)
