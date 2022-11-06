import sys

N = sys.stdin.readline().strip()
my_list = [0 for _ in range(9)]
for i in N:
    if i == '9':
        my_list[6] += 1
    else:
        my_list[int(i)] += 1

a = my_list[6]

if a % 2 == 0:
    my_list[6] = a // 2
else:
    my_list[6] = a // 2 + 1

print(max(my_list))
