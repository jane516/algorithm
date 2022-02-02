import sys


def 넓이(x1, y1, x2, y2, x3, y3):
    P = x1 * y2 + x2 * y3 + x3 * y1
    M = x2 * y1 + x3 * y2 + x1 * y3
    S = abs(P - M)
    return S


N = int(input())
xy_list = [[0 for _ in range(2)] for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    xy_list[i][0] = int(case[0])
    xy_list[i][1] = int(case[1])
if N == 3:
    S = 넓이(xy_list[0][0], xy_list[0][1], xy_list[1][0], xy_list[1][1], xy_list[2][0], xy_list[2][1])
    print(round(S/2, 1))
else:
    x1 = (xy_list[0][0] + xy_list[N//2 - 1][0]) // 2
    y1 = (xy_list[0][1] + xy_list[N//2 - 1][1]) // 2
    sum = 0
    for i in range(N-1):
        sum += 넓이(x1, y1, xy_list[i][0], xy_list[i][1], xy_list[i+1][0], xy_list[i+1][1])
    sum += 넓이(x1, y1, xy_list[-1][0], xy_list[-1][1], xy_list[0][0], xy_list[0][1])
    print(round(sum / 2, 1))