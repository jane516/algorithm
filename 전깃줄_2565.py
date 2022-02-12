import sys
N = int(input())
A = [[0 for _ in range(2)] for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    x, y = int(case[0]), int(case[1])
    A[i][0], A[i][1] = x, y
A.sort()
DP = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if A[i][1] > A[j][1]:
            DP[i] = max(DP[i], DP[j] + 1)
print(N - max(DP))