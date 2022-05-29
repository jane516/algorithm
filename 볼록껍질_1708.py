import sys
N = int(sys.stdin.readline().strip())
xy_list = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(N)]
xy_list.sort(key=lambda x: (x[1], x[0]))
x, y = xy_list[0][0], xy_list[0][1]


def cross_product(x1, y1, x2, y2, x3, y3):
    P = x1 * y2 + x2 * y3 + x3 * y1
    M = x2 * y1 + x3 * y2 + x1 * y3
    return P - M


def merge_sort(my_list):
    if len(my_list) == 1:
        return my_list
    mid = len(my_list) // 2
    list1 = merge_sort(my_list[:mid])
    list2 = merge_sort(my_list[mid:])

    i, j = 0, 0
    arr = []

    while i < len(list1) and j < len(list2):
        x1, y1 = list1[i][0], list1[i][1]
        x2, y2 = list2[j][0], list2[j][1]
        k = cross_product(x, y, x1, y1, x2, y2)
        if k < 0:
            arr.append(list1[i])
            i += 1
        elif k == 0:
            d1 = (x1 - x) ** 2 + (y1 - y) ** 2
            d2 = (x2 - x) ** 2 + (y2 - y) ** 2
            if d1 < d2:
                arr.append(list1[i])
                i += 1
            else:
                arr.append(list2[j])
                j += 1
        else:
            arr.append(list2[j])
            j += 1
    arr += list1[i:]
    arr += list2[j:]
    return arr


xy_list = merge_sort(xy_list)
xy_list.append([x, y])
stack = [[x, y], [xy_list[1][0], xy_list[1][1]]]
for i in range(1, N + 1):
    while len(stack) >= 2 \
            and cross_product(stack[-2][0], stack[-2][1],
                              stack[-1][0], stack[-1][1],
                              xy_list[i][0], xy_list[i][1]) >= 0:
        stack.pop()
    stack.append([xy_list[i][0], xy_list[i][1]])

print(len(stack) - 1)