import sys

N = int(sys.stdin.readline().strip())
for i in range(N):
    len_list = list(map(int, sys.stdin.readline().strip().split()))
    len_list.sort()
    print(f'Scenario #{i + 1}:')
    if len_list[0] ** 2 + len_list[1] ** 2 == len_list[2] ** 2:
        print('yes')
        print()
    else:
        print('no')
        print()
