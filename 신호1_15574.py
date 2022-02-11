import sys


def d(x1, y1, x2, y2):
    return ((x1 - x2)**2 + (y1 - y2)**2)**0.5


N = int(input())
xy_list = [[0 for _ in range(2)] for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    xy_list[i][0] = int(case[0])
    xy_list[i][1] = int(case[1])

xy_list.sort()
my_list = [[] for _ in range(N)]
my_list[0] = [xy_list[0][0], xy_list[0][1]]
DP = [[0 for _ in range(2)] for _ in range(N)]

if N == 1:
    print(0)
else:
    Sum = 0
    k = 0
    for i in range(1, N):
        if i == N - 1:
            my_list[k].append(xy_list[-1][0])
            my_list[k].append(xy_list[-1][1])
        if xy_list[i][0] != xy_list[i-1][0]:
            my_list[k].append(xy_list[i-1][0])
            my_list[k].append(xy_list[i-1][1])
            k += 1
            my_list[k].append(xy_list[i][0])
            my_list[k].append(xy_list[i][1])
    if k == 0:
        print(0)
    else:
        for i in range(1, k+1):
            d1 = d(my_list[i][0], my_list[i][1], my_list[i - 1][-2], my_list[i - 1][-1])
            d2 = d(my_list[i][0], my_list[i][1], my_list[i - 1][0], my_list[i - 1][1])
            d3 = d(my_list[i][-2], my_list[i][-1], my_list[i - 1][-2], my_list[i - 1][-1])
            d4 = d(my_list[i][-2], my_list[i][-1], my_list[i - 1][0], my_list[i - 1][1])
            DP[i][0] = max(DP[i-1][0] + d2, DP[i-1][1] + d1)
            DP[i][1] = max(DP[i-1][0] + d4, DP[i-1][1] + d3)
        print(max(DP[k]))

