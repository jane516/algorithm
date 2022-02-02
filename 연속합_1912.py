import sys
n, m = map(int, input().split())
case = list(sys.stdin.readline().strip().split())
my_list = [0] * n
for i in range(n):
    my_list[i] = int(case[i])
sum_list = [0] * n
sum_list[0] = my_list[0]
for i in range(1, n):
    sum_list[i] = max(my_list[i], my_list[i] + sum_list[i-1])
print(sum_list)