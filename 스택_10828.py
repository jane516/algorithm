import sys

N = int(input())
stack = []
for i in range(N):
    case = sys.stdin.readline().strip()
    a = case.split(" ")[0]
    if a == 'push':
        b = int(case.split(" ")[1])
        stack.append(b)
    if a == 'pop':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])
            stack.pop()
    if a == 'size':
        print(len(stack))
    if a == 'empty':
        if len(stack) == 0:
            print(1)
        else:
            print(0)
    if a == 'top':
        if len(stack) == 0:
            print(-1)
        else:
            print(stack[-1])