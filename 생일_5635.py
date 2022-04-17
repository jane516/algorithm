import sys
n = int(input())
my_list = []
for i in range(n):
    case = sys.stdin.readline().strip().split()
    my_list.append([int(case[3]), int(case[2]), int(case[1]), case[0]])
my_list.sort()
print(my_list[-1][3])
print(my_list[0][3])