import sys
n = int(sys.stdin.readline().strip())
case = sys.stdin.readline().strip().split()
box_list = [0 for _ in range(n)]
for i in range(n):
    box_list[i] = int(case[i])
dp = [1 for _ in range(n)]
for i in range(n):
    for j in range(i):
        if box_list[i] > box_list[j]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))