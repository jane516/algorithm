import sys
N = int(input())
R = []
G = []
B = []
dp = [[0 for _ in range(3)] for _ in range(N+1)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    R.append(int(case[0]))
    G.append(int(case[1]))
    B.append(int(case[2]))

dp[1][0] = R[0]
dp[1][1] = G[0]
dp[1][2] = B[0]
for i in range(2, N + 1):
    dp[i][0] = min(dp[i - 1][1], dp[i - 1][2]) + R[i - 1]
    dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + G[i - 1]
    dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + B[i - 1]
print(dp[N])