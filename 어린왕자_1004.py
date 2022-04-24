import sys

T = int(input())
for _ in range(T):
    case = sys.stdin.readline().strip().split()
    x_1, y_1, x_2, y_2 = int(case[0]), int(case[1]), int(case[2]), int(case[3])
    n = int(input())
    count = 0
    for i in range(n):
        case2 = sys.stdin.readline().strip().split()
        c_x, c_y, r = int(case2[0]), int(case2[1]), int(case2[2])
        if (x_1 - c_x)**2 + (y_1 - c_y)**2 < r**2 \
                and (x_2 - c_x)**2 + (y_2 - c_y)**2 > r**2:
            count += 1
        if (x_2 - c_x)**2 + (y_2 - c_y)**2 < r**2 \
            and (x_1 - c_x)**2 + (y_1 - c_y)**2 > r**2:
            count += 1
    print(count)