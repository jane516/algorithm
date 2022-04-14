import sys
N = int(input())
xy_list = [[0 for _ in range(2)] for _ in range(N + 1)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    xy_list[i][0] = int(case[0])
    xy_list[i][1] = int(case[1])
    if i == 0:
        xy_list[N][0] = int(case[0])
        xy_list[N][1] = int(case[1])
Sum1 = 0
Sum2 = 0
for i in range(N):
    Sum1 += xy_list[i][0] * xy_list[i+1][1]
    Sum2 += xy_list[i][1] * xy_list[i+1][0]
print(abs(Sum1 - Sum2) / 2)