import sys

S = list(sys.stdin.readline().strip())
M = int(sys.stdin.readline().strip())
my_list = []

for _ in range(M):
    order = list(sys.stdin.readline().strip().split())
    if order[0] == 'P':
        S.append(order[1])
    elif order[0] == 'L':
        if S:
            X = S.pop()
            my_list.append(X)
        else:
            continue
    elif order[0] == 'D':
        if my_list:
            X = my_list.pop()
            S.append(X)
        else:
            continue
    else:
        if S:
            S.pop()
for i in range(len(my_list)):
    S.append(my_list[len(my_list) - 1 - i])
for i in S:
    print(i, end='')