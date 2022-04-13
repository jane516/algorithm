import sys
N, K = map(int, input().split())
weight_list = []
value_list = []
dp = [[0 for _ in range(K + 1)] for _ in range(N + 1)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    weight_list.append(int(case[0]))
    value_list.append(int(case[1]))
for i in range(1, N + 1):
    for j in range(1, K + 1):
        if weight_list[i-1] <= j:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight_list[i-1]] + value_list[i-1])
        else:
            dp[i][j] = dp[i-1][j]
print(dp[N][K])