import sys
case = list(sys.stdin.readline().strip())
P_list = ['P', 'P', 'A', 'P']
my_list = []
for i in case:
    count = 0
    my_list.append(i)
    if len(my_list) >= 4 and i == P_list[-1]:
        for j in range(4):
            if my_list[-1-j] == P_list[-1-j]:
                count += 1
        if count == 4:
            for j in range(4):
                my_list.pop()
            my_list.append('P')
if len(my_list) == 1 and my_list[0] == 'P':
    print('PPAP')
else:
    print('NP')