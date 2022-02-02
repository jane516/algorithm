import sys


def cross_product(x1, y1, x2, y2, x3, y3):
    answer = 0
    P = x1 * y2 + x2 * y3 + x3 * y1
    M = x2 * y1 + x3 * y2 + x1 * y3
    if P - M < 0:
        answer = -1  # 시계 방향
    elif P - M == 0:
        answer = 0
    else:
        answer = 1  # 반시계 방향
    return answer


case1 = sys.stdin.readline().strip().split()
case2 = sys.stdin.readline().strip().split()
x1, y1, x2, y2 = int(case1[0]), int(case1[1]), int(case1[2]), int(case1[3])
x3, y3, x4, y4 = int(case2[0]), int(case2[1]), int(case2[2]), int(case2[3])
result1 = cross_product(x1, y1, x2, y2, x3, y3)
result2 = cross_product(x1, y1, x2, y2, x4, y4)
result3 = cross_product(x3, y3, x4, y4, x1, y1)
result4 = cross_product(x3, y3, x4, y4, x2, y2)
result = 0
if result1 * result2 == 0 and result3 * result4 == 0:
    if min(x1, x2) <= max(x3, x4) and min(x3, x4) <= max(x1, x2) and min(y1, y2) <= max(y3, y4) and min(y3, y4) <= max(y1, y2):
        result = 1
elif result1 * result2 <= 0 and result3 * result4 <= 0:
    result = 1
print(result)