import sys


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


case1 = sys.stdin.readline().strip()
a = int(case1.split()[0])
d = int(case1.split()[1])
A = [0] * 1000001
for i in range(1000000):
    A[0] = 0
    A[1] = a
    A[i] = A[i-1] + a + d * (i-1)
q = int(input())
for i in range(q):
    case2 = sys.stdin.readline().strip()
    l = int(case2.split()[1])
    r = int(case2.split()[2])
    Sum = 0
    B = []
    GCD = A[l] - A[l-1]
    if int(case2.split()[0]) == 1:
        print(A[r] - A[l-1])
    else:
        for k in range(1, r-l+1):
            GCD = gcd(GCD, A[l+k] - A[l+k-1])
        print(GCD)

