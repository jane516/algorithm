import sys

N = int(sys.stdin.readline().strip())

A_list = list(map(int, sys.stdin.readline().strip().split()))
stack = []
result = [0 for _ in range(N)]

for i in range(N):
    while stack and A_list[stack[-1]] < A_list[N - 1 - i]:
        result[stack.pop()] = N - i
    stack.append(N - 1 - i)

print(*result)