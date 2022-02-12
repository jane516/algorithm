import sys
N = int(input())
case = sys.stdin.readline().strip().split()
A = [0 for _ in range(N)]
for i in range(N):
    A[i] = int(case[i])
DP = [1 for _ in range(N)]
B = []
for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            DP[i] = max(DP[i], DP[j] + 1)
print(max(DP))
k = DP.index(max(DP))
M = max(DP)
B.append(A[k])
for i in range(k, -1, -1):
    if DP[i] == M-1 and A[i] < A[k]:
        B.append(A[i])
        M = DP[i]
B.reverse()
print(*B)