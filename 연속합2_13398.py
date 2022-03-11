import sys
n = int(sys.stdin.readline().strip())
case = sys.stdin.readline().strip().split()
num_list = []
result = -1000

for i in range(n):
    num_list.append(int(case[i]))

dp = [[0 for _ in range(2)] for _ in range(n)]
dp[0][0] = num_list[0]

for i in range(1, n):
    dp[i][0] = max(dp[i-1][0] + num_list[i], num_list[i])
    dp[i][1] = max(dp[i-1][0], dp[i-1][1] + num_list[i])
    result = max(result, max(dp[i][0], dp[i][1]))

if len(num_list) == 1:
    print(num_list[0])
else:
    result = max(result, num_list[0])
    print(result)