import sys
case1 = sys.stdin.readline().strip()
case2 = sys.stdin.readline().strip()
case3 = sys.stdin.readline().strip()
dp = [[[0 for _ in range(len(case1) + 1)] for _ in range(len(case2) + 1)] for _ in range(len(case3) + 1)]
for k in range(1, len(case3) + 1):
    for i in range(1, len(case2) + 1):
        for j in range(1, len(case1) + 1):
            if case2[i-1] == case1[j-1] == case3[k - 1]:
                dp[k][i][j] = dp[k-1][i-1][j-1] + 1
            else:
                dp[k][i][j] = max(dp[k-1][i][j], dp[k][i-1][j], dp[k][i][j-1])
print(dp[-1][-1][-1])