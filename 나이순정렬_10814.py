import sys

N = int(input())
my_list = [[0 for _ in range(3)] for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    my_list[i][0], my_list[i][1], my_list[i][2] = int(case[0]), i, case[1]
my_list.sort()
for i in my_list:
    print(i[0], i[2])