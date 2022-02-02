dp = [0] * 1001
dp[1] = 2
for i in range(2, 1001):
    dp[i] = dp[i-1] * (4 * i - 2) // i
while True:
    N = int(input())
    if N == 0:
        break
    print(dp[N] // (N + 1))