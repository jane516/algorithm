from bisect import bisect_left
import sys
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
L = [A[0]]
for i in range(1, N):
    if L[-1] < A[i]:
        L.append(A[i])
    else:
        idx = bisect_left(L, A[i])
        L[idx] = A[i]
print(len(L))