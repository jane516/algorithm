import sys

while True:
    stack = []

    Max = 0
    h_list = list(map(int, sys.stdin.readline().strip().split()))
    n = h_list[0]

    if n == 0:
        break

    h_list = h_list[1:]
    for i in range(n):
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
            width = n
        else:
            width = n - stack[-1] - 1
        Max = max(Max, width * h_list[idx])

    print(Max)

