import sys


def e_gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return [a, 1, 0]
    else:
        x1, x2 = 1, 0
        y1, y2 = 0, 1
        while b > 0:
            q = a // b
            r = a % b
            x = x1 - q * x2
            y = y1 - q * y2
            a, b = b, r
            x1, x2 = x2, x
            y1, y2 = y2, y
        return [a, x1, y1]


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


T = int(input())
for i in range(T):
    case = sys.stdin.readline().strip()
    K, C = int(case.split()[0]), int(case.split()[1])
    if gcd(K, C) != 1:
        print('IMPOSSIBLE')
    else:
        if C == 1:
            if K < 10 ** 9:
                print(K+1)
            else:
                print('IMPOSSIBLE')
        elif K == 1:
            print(1)
        else:
            if K > C:
                print(e_gcd(K, C)[2] % K)
            else:
                print(e_gcd(K, C)[1] % K)