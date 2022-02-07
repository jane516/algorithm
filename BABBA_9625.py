K = int(input())
DP = [[0 for _ in range(2)] for _ in range(46)]

DP[1][0] = 0
DP[1][1] = 1
DP[2][0] = 1
DP[2][1] = 1

for i in range(3, K + 1):
    DP[i][0] = DP[i-1][0] + DP[i-2][0]
    DP[i][1] = DP[i-1][1] + DP[i-2][1]

print(DP[K][0], DP[K][1])
