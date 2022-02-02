import sys
case = list(sys.stdin.readline().strip())
bomb = list(input())
my_list = []
for i in case:
    count = 0
    my_list.append(i)
    if len(my_list) >= len(bomb) and i == bomb[-1]:
        for j in range(len(bomb)):
            if my_list[-1-j] == bomb[-1-j]:
                count += 1
        if count == len(bomb):
            for j in range(len(bomb)):
                my_list.pop()
if len(my_list) == 0:
    print('FRULA')
else:
    print(''.join(my_list))
