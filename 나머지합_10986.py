import sys


def Combination(n, r):
    if n-r < r:
        r = n-r
    분모 = 분자 = 1
    for i in range(r):
        분자 *= (n-i)
        분모 *= (i+1)
    return 분자 // 분모


N, M = map(int, input().split())
case = sys.stdin.readline().strip().split()
A = []
B = [0] * M
for i in range(N):
    A.append(int(case[i]))
A[0] %= M
for i in range(N):
    if i == 0:
        A[i] %= M
    else:
        A[i] = (A[i-1] + A[i]) % M
    B[A[i]] += 1
result = 0
for i in B[1:]:
    if i == 0 or i == 1:
        continue
    else:
        result += Combination(i, 2)
if B[0] != 0:
    result += Combination(B[0]+1, 2)
print(result)