import sys
N = int(sys.stdin.readline().strip())
xy_list = [(0, 0) for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    xy_list[i] = (int(case[0]), int(case[1]))
xy_list.sort()
start, end = xy_list[0][0], xy_list[0][1]
result = 0
for i in range(1, N):
    if xy_list[i][0] > end:
        result += end - start
        start = xy_list[i][0]
        end = xy_list[i][1]
    else:
        end = max(xy_list[i][1], end)
result += end - start
print(result)