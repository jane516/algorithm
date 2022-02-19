import sys
N = int(sys.stdin.readline().strip())
xy_list = [[0 for _ in range(2)] for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    xy_list[i][0], xy_list[i][1] = int(case[0]), int(case[1])
xy_list.sort()
for i in xy_list:
    print(i[0], i[1])