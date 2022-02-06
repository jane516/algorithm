import sys
N = int(sys.stdin.readline().strip())
time_list = []
for i in range(N):
    case = sys.stdin.readline().strip().split()
    start, end = int(case[0]), int(case[1])
    time_list.append([start, end])
time_list.sort()
stack = [time_list[0]]
for i in time_list[1:]:
    if stack[-1][1] > i[-1]:
        stack.pop()
        stack.append(i)
    else:
        if stack[-1][1] <= i[0]:
            stack.append(i)
print(len(stack))