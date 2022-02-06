import sys
N = int(input())
xr_list = []
for i in range(N):
    case = sys.stdin.readline().strip().split()
    x, r = int(case[0]), int(case[1])
    xr_list.append([x - r, 0, i])
    xr_list.append([x + r, 1, i])
xr_list.sort()

stack = [xr_list[0]]
for i in xr_list[1:]:
    if len(stack) >= 1 and stack[-1][2] == i[2]:
        stack.pop()
    else:
        stack.append(i)
if len(stack) == 0:
    print('YES')
else:
    print('NO')