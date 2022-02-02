import sys


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


N = int(input())
A = [0] * N
B = []
case = sys.stdin.readline().strip().split()
for i in range(N):
    A[i] = int(case[i])
A.sort()

for i in range(N-1):
    B.append(A[i+1]-A[i])

B.sort()
GCD = B[0]
for i in range(N-2):
    if B[i] == 0 and B[i+1] == 0:
        continue
    elif B[i] == 0 and B[i+1] != 0:
        GCD = B[i + 1]
    else:
        GCD = min(GCD, gcd(B[i], B[i+1]))


print(GCD)