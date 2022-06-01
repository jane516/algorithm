import sys
T = int(sys.stdin.readline().strip())
for _ in range(T):
    n, m = map(int, sys.stdin.readline().strip().split())
    bxy_list = [[0, 0, 0] for _ in range(n)]
    for i in range(n):
        x, y = map(int, sys.stdin.readline().strip().split())
        bxy_list[i][0], bxy_list[i][1] = x, y
    bxy_list.sort(key=lambda x: (x[1], x[0]))
    a, b = bxy_list[0][0], bxy_list[0][1]
    wxy_list = [[0, 0, 1] for _ in range(m)]
    for i in range(m):
        x, y = map(int, sys.stdin.readline().strip().split())
        wxy_list[i][0], wxy_list[i][1] = x, y
    wxy_list.sort(key=lambda x: (x[1], x[0]))
    c, d = wxy_list[0][0], wxy_list[0][1]


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


    check = 0
    xy_list = merge_sort(xy_list)
    if xy_list[0][2] == 0:
        for j in range(n):
            if xy_list[j][2] == 1:
                check = 1
                break
        if check == 0:
            print('YES')
    else:
        for j in range(m):
            if xy_list[j][2] == 0:
                check = 1
                break
        if check == 0:
            print('YES')
    if check == 1:
        bxy_list.sort()
        wxy_list.sort()
        if bxy_list[-1][0] <= wxy_list[0][0] or wxy_list[-1][0] <= bxy_list[0][0]:
            print('YES')
        else:
            bxy_list.sort(key=lambda x: (x[1], x[0]))
            wxy_list.sort(key=lambda x: (x[1], x[0]))
            if bxy_list[-1][1] <= wxy_list[0][1] or wxy_list[-1][1] <= bxy_list[0][1]:
                print('YES')
            else:
                print('NO')

