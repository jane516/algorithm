import sys
n, k = map(int, input().split())
coin = [0 for _ in range(n)]
for i in range(n):
    coin[i] = int(sys.stdin.readline().strip())
dp = [10001 for _ in range(k + 1)]
dp[0] = 0
for i in range(n):
    for j in range(coin[i], k + 1):
        dp[j] = min(dp[j], dp[j - coin[i]] + 1)
if dp[k] == 10001:
    print(-1)
else:
    print(dp[k])