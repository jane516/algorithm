import sys


def 수직(x1, y1, x2, y2, x3, y3):  # x1, y1을 시작점
    result = (x1 - x2) * (x1 - x3) + (y1 - y2) * (y1 - y3)
    if result == 0:
        return 1
    else:
        return 0


T = int(input())
for i in range(T):
    xy_list = [[0 for _ in range(2)] for _ in range(4)]
    A = []
    answer = 0
    for j in range(4):
        case = sys.stdin.readline().strip().split()
        xy_list[j][0], xy_list[j][1] = int(case[0]), int(case[1])
    xy_list.sort()
    d1 = (xy_list[1][0] - xy_list[0][0]) ** 2 + (xy_list[1][1] - xy_list[0][1]) ** 2
    d2 = (xy_list[1][0] - xy_list[3][0]) ** 2 + (xy_list[1][1] - xy_list[3][1]) ** 2
    if 수직(xy_list[1][0], xy_list[1][1], xy_list[0][0], xy_list[0][1], xy_list[3][0], xy_list[3][1]):
        if 수직(xy_list[2][0], xy_list[2][1], xy_list[0][0], xy_list[0][1], xy_list[3][0], xy_list[3][1]):
            if d1 == d2:
                answer = 1
    print(answer)

