import sys
case = sys.stdin.readline().strip().split()
N, M = int(case[0]), int(case[1])
my_list = []
check_list = []
for i in range(N):
    word = sys.stdin.readline().strip()
    my_list.append([word, 0])
for i in range(M):
    count = 0
    case2 = sys.stdin.readline().strip().split()
    if case2[0] == '1':
        for j in range(N):
            if case2[1] in my_list[j][0]:
                my_list[j][1] += 1
    else:
        for j in range(N):
            if case2[1] in my_list[j][0]:
                my_list[j][1] -= 1
    for j in range(N):
        if my_list[j][1] == 0:
            count += 1
    print(count)
