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


n = int(sys.stdin.readline().strip())
case = sys.stdin.readline().strip().split()
k = int(sys.stdin.readline().strip())
check = 0
A = []
for i in range(n):
    A.append(cross_product(0, 0, 1, k, i+1, int(case[i])))
마이너스 = A.count(-1)
영 = A.count(0)
플러스 = A.count(1)
if 마이너스 == n or 플러스 == n:
    print('F')
else:
    print('T')
