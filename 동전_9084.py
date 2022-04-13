import sys
T = int(input())
for i in range(T):
    N = int(input())
    case = sys.stdin.readline().strip().split()
    coin = [int(case[j]) for j in range(N)]
    M = int(input())
    dp = [0 for _ in range(M + 1)]
    dp[0] = 1
    for j in coin:
        for k in range(j, M + 1):
            dp[k] += dp[k - j]
    print(dp[M])