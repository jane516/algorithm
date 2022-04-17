import sys
n = int(sys.stdin.readline().strip())
pay_list = []
M = 0
Sum = 0
for i in range(n):
    case = sys.stdin.readline().strip().split()
    pay_list.append([int(case[0]), int(case[1])])
    if int(case[1]) > M:
        M = int(case[1])
pay_list.sort()
day_list = [0 for _ in range(M)]
for i in range(n):
    day = pay_list[-1-i][1]
    while True:
        if day == 0:
            break
        if day_list[day-1] == 0:
            Sum += pay_list[-1-i][0]
            day_list[day-1] = 1
            break
        else:
            day -= 1
print(Sum)