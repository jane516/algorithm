import sys
for i in range(3):
    my_list = list(sys.stdin.readline().strip().split())
    x = my_list.count('0')
    dic = {0: 'E', 1: 'A', 2: 'B', 3: 'C', 4: 'D'}
    print(dic[x])