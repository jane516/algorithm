import sys
N = int(sys.stdin.readline().strip())
minus_list = []
plus_list = []
for i in range(N):
    case = sys.stdin.readline().strip().split()
    x, y = int(case[0]), int(case[1])
    minus_list.append(x-y)
    plus_list.append(x+y)
minus_list.sort()
plus_list.sort()
print(max(minus_list[-1]-minus_list[0], plus_list[-1]-plus_list[0]))