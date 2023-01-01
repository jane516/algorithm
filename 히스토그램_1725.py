import sys

N = int(sys.stdin.readline().strip())
h_list = [0 for _ in range(N)]

for i in range(N):
    h_list[i] = int(sys.stdin.readline().strip())

stack = []

Max = 0


for i in range(N):
    while len(stack) != 0 and h_list[stack[-1]] >= h_list[i]:
        idx = stack.pop()

        if len(stack) == 0:
            width = i
        else:
            width = i - stack[-1] - 1
        Max = max(Max, width * h_list[idx])
    stack.append(i)

while len(stack) != 0:
    idx = stack.pop()

    if len(stack) == 0:
        width = N
    else:
        width = N - stack[-1] - 1
    Max = max(Max, width * h_list[idx])

print(Max)