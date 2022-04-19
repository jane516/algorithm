import sys
from bisect import bisect_left
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
B = list(map(int, sys.stdin.readline().strip().split()))
C = [0 for _ in range(N)]
for i in range(N):
    C[i] = A.index(B[i])
L = [C[0]]
for i in range(1, N):
    if L[-1] < C[i]:
        L.append(C[i])
    else:
        index = bisect_left(L, C[i])
        L[index] = C[i]
print(len(L))