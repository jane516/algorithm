import sys
n = int(sys.stdin.readline().strip())
Square = [i**2 for i in range(1, 225)]
dp = [i for i in range(n + 1)]
for i in Square:
    for j in range(i, n + 1):
        dp[j] = min(dp[j], dp[j - i] + 1)
print(dp[n])