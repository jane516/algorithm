import sys
case1 = sys.stdin.readline().strip().split()
x_1 = int(case1[0])
y_1 = int(case1[1])
r_1 = int(case1[2])

case2 = sys.stdin.readline().strip().split()
x_2 = int(case2[0])
y_2 = int(case2[1])
r_2 = int(case2[2])

d = (x_1 - x_2) ** 2 + (y_1 - y_2) ** 2

if d < (r_1 + r_2) ** 2:
    print('YES')
else:
    print('NO')