import sys


def power(a, n):
    if n == 1:
        return a
    else:
        b = power(a, n // 2)
        if n % 2 == 0:
            return b * b % 1000000007
        else:
            return a * b * b % 1000000007


M = int(input())
Fac = [0] * 4000001
Fac[0] = 1
for i in range(1, 4000001):
    Fac[i] = Fac[i-1] * i % 1000000007
for j in range(M):
    case = sys.stdin.readline().strip()
    N = int(case.split()[0])
    K = int(case.split()[1])
    R = Fac[N] * power(Fac[K] * Fac[N-K], 1000000005) % 1000000007
    print(R)