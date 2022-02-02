N = int(input())
dp = [0] * 100001
dp[1] = 1
dp[2] = 2
for i in range(1, N + 1):
    if int(i ** 0.5) ** 2 == i:
        dp[i] = 1
    else:
        최소개수 = i
        for j in range(1, int(i ** 0.5) + 1):
            최소개수 = min(최소개수, dp[j**2] + dp[i - j**2])
        dp[i] = 최소개수
print(dp[N])