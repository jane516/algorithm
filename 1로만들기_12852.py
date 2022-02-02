N = int(input())
dp = [0] * 1000001
dp[1] = 0
A = []
for i in range(2, N + 1):
    dp[i] = dp[i-1] + 1
    A.append(N-i)
    if i % 2 == 0:
        dp[i] = min(dp[i], dp[i//2] + 1)
    if i % 3 == 0:
        dp[i] = min(dp[i], dp[i//3] + 1)
print(dp[N])