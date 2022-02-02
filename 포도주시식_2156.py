n = int(input())
A = [0] * n
for i in range(n):
    A[i] = int(input())
dp = [[0 for _ in range(3)] for _ in range(10001)]
dp[1][1] = A[0]
dp[1][2] = 0
if n > 1:
    dp[2][1] = A[1]
    dp[2][2] = A[0] + A[1]
    for j in range(3, n + 1):
        dp[j][1] = max(max(dp[j-2]), max(dp[j-3])) + A[j-1]
        dp[j][2] = dp[j-1][1] + A[j-1]
if n == 1:
    print(max(dp[n]))
else:
    print(max(max(dp[n-1]), max(dp[n])))