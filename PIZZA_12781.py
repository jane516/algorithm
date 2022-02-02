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


case = sys.stdin.readline().strip().split()
x1, y1, x2, y2 = int(case[0]), int(case[1]), int(case[2]), int(case[3])
x3, y3, x4, y4 = int(case[4]), int(case[5]), int(case[6]), int(case[7])
result1 = cross_product(x1, y1, x2, y2, x3, y3)
result2 = cross_product(x1, y1, x2, y2, x4, y4)
result3 = cross_product(x3, y3, x4, y4, x1, y1)
result4 = cross_product(x3, y3, x4, y4, x2, y2)
result = 0
if result1 * result2 < 0 and result3 * result4 < 0:
    result = 1
print(result)