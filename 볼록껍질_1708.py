import sys
N = int(sys.stdin.readline().strip())
xy_list = [[0, 0] for _ in range(N)]
xy_list2 = xy_list[:]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    xy_list[i] = [int(case[0]), int(case[1])]
    xy_list2[i] = [int(case[1]), int(case[0])]
xy_list.sort()
xy_list2.sort()


def cross_product(x1, y1, x2, y2, x3, y3):
    P = x1 * y2 + x2 * y3 + x3 * y1
    M = x2 * y1 + x3 * y2 + x1 * y3
    return P - M


my_list = [[0, 0, 0, 0] for _ in range(N - 1)]
x1, y1 = xy_list[0][0], xy_list[0][1]
if xy_list2[0][1] == xy_list[0][0] and xy_list2[0][0] == xy_list[0][1]:
    x2, y2 = xy_list2[1][1], xy_list2[1][0]
else:
    x2, y2 = xy_list2[0][1], xy_list2[0][0]
d1 = (x2 - x1) ** 2 + (y2 - y1) ** 2
v1 = [x2 - x1, y2 - y1]
for i in range(1, N):
    x3, y3 = xy_list[i][0], xy_list[i][1]
    d2 = (x3 - x1) ** 2 + (y3 - y1) ** 2
    v2 = [x3 - x1, y3 - y1]
    k = (v1[0] * v2[0] + v1[1] * v2[1])
    if k < 0:
        my_list[i-1][0] = -k**2 / (d1 * d2)
    else:
        my_list[i - 1][0] = k ** 2 / (d1 * d2)
    my_list[i-1][1] = (x1-x3)**2 + (y1-y3)**2
    my_list[i-1][2], my_list[i-1][3] = x3, y3
my_list.sort()
my_list.append([0, 0, x1, y1])

stack = [[x1, y1], [my_list[0][2], my_list[0][3]]]
for i in range(1, N):
    while len(stack) >= 2 \
            and cross_product(stack[-2][0], stack[-2][1],
                              stack[-1][0], stack[-1][1],
                              my_list[i][2], my_list[i][3]) >= 0:
        stack.pop()
    stack.append([my_list[i][2], my_list[i][3]])

print(len(stack) - 1)