import sys
N = int(input())
case = sys.stdin.readline().strip().split()
A = [0 for _ in range(N)]
DP = [1 for _ in range(N)]
for i in range(N):
    A[i] = int(case[i])
for i in range(N):
    for j in range(i):
        if A[i] < A[j]:
            DP[i] = max(DP[i], DP[j] + 1)
print(max(DP))