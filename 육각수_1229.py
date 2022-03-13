import sys
N = int(sys.stdin.readline().strip())
육각수 = [2 * i**2 - i for i in range(1, 709)]

dp = [6 for _ in range(N + 1)]
dp[0] = 0


for i in range(708):
    for j in range(육각수[i], N + 1):
        if 육각수[i] <= j:
            dp[j] = min(dp[j], dp[j - 육각수[i]] + 1)
        else:
            break

print(dp[N])