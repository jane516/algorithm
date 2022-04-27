import sys
N = int(sys.stdin.readline().strip())
xy_list = [[0, 0] for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    xy_list[i] = [int(case[0]), int(case[1])]
xy_list.sort()


def cross_product(x1, y1, x2, y2, x3, y3):
    P = x1 * y2 + x2 * y3 + x3 * y1
    M = x2 * y1 + x3 * y2 + x1 * y3
    return P - M


my_list = [[0, 0, 0, 0] for _ in range(N - 1)]
x2, y2, x1, y1 = xy_list[0][0], xy_list[0][1], xy_list[0][0] - 1, xy_list[0][1]
for i in range(1, N):
    my_list[i-1][0] = cross_product(x1, y1, x2, y2, xy_list[i][0], xy_list[i][1])
    my_list[i-1][1] = (x1-xy_list[i][0])**2 + (y1-xy_list[i][1])**2
    my_list[i-1][2], my_list[i-1][3] = xy_list[i][0], xy_list[i][1]
my_list.sort()
my_list.append([0, 0, xy_list[0][0], xy_list[0][1]])

stack = [[xy_list[0][0], xy_list[0][1]], [my_list[0][2], my_list[0][3]]]
for i in range(1, N):
    while len(stack) >= 2 \
            and cross_product(stack[-2][0], stack[-2][1],
                              stack[-1][0], stack[-1][1],
                              my_list[i][2], my_list[i][3]) <= 0:
        stack.pop()
    stack.append([my_list[i][2], my_list[i][3]])

print(len(stack) - 1)