DP = [[0 for _ in range(4)] for _ in range(100001)]
DP[1] = [0, 1, 0, 0]
DP[2] = [0, 0, 1, 0]
DP[3] = [0, 1, 1, 1]
DP[4] = [0, 2, 0, 1]
DP[5] = [0, 1, 2, 1]
for i in range(6, 100001):
    DP[i][1] = (DP[i-1][2] + DP[i-1][3]) % 1000000009
    DP[i][2] = (DP[i-2][1] + DP[i-2][3]) % 1000000009
    DP[i][3] = (DP[i-3][1] + DP[i-3][2]) % 1000000009
T = int(input())
for i in range(T):
    print(sum(DP[int(input())]) % 1000000009)
