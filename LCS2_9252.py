import sys
case1 = sys.stdin.readline().strip()
case2 = sys.stdin.readline().strip()
dp = [[0 for _ in range(len(case1) + 1)] for _ in range(len(case2) + 1)]
for i in range(1, len(case2) + 1):
    for j in range(1, len(case1) + 1):
        if case2[i-1] == case1[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
result = ''
now = dp[-1][-1]
x = len(case2)
y = len(case1)
while True:
    if dp[x][y-1] == now - 1 and dp[x-1][y] == now - 1:
        result = case2[x-1] + result
        now -= 1
        x -= 1
        y -= 1
    else:
        if dp[x-1][y] > dp[x][y-1]:
            x -= 1
        else:
            y -= 1
    if now == 0:
        break
print(dp[-1][-1])
print(result)