import sys
import math
from itertools import combinations
T = int(input())
for _ in range(T):
    N = int(input())
    xy_list = [[0, 0] for _ in range(N)]
    xtotal, ytotal = 0, 0
    for i in range(N):
        case = sys.stdin.readline().strip().split()
        x, y = int(case[0]), int(case[1])
        xy_list[i] = x, y
        xtotal += x
        ytotal += y
    min = math.inf
    com = list(combinations(range(N), N // 2))
    for i in com[:len(com) // 2]:
        xsum, ysum = 0, 0
        for j in i:
            xsum += xy_list[j][0]
            ysum += xy_list[j][1]
        xsum -= xtotal - xsum
        ysum -= ytotal - ysum

        result = math.sqrt(xsum ** 2 + ysum ** 2)
        if min > result:
            min = result
    print(min)