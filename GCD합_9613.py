import sys


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


n = int(input())
for i in range(n):
    case = sys.stdin.readline().strip()
    a = list(map(int, case.split()))
    b = []
    for j in range(1, a[0]):
        for k in range(j+1, a[0] + 1):
            b.append(gcd(a[j], a[k]))
    print(sum(b))