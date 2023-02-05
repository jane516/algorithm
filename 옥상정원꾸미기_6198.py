import sys

N = int(sys.stdin.readline().strip())
buildings = [0 for _ in range(N)]

for i in range(N):
    buildings[i] = int(sys.stdin.readline().strip())


def bench_marking(N, buildings):
    result = [0] * N
    stack = []
    for i in range(N):
        while stack and buildings[stack[-1]] <= buildings[i]:
            stack.pop()
        result[i] = len(stack)
        stack.append(i)
    return sum(result)


print(bench_marking(N, buildings))