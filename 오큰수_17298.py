import sys

N = int(sys.stdin.readline().strip())

A_list = list(map(int, sys.stdin.readline().strip().split()))
stack = []
result = [-1 for _ in range(N)]

for i in range(N):
    while stack and A_list[stack[-1]] < A_list[i]:
        result[stack.pop()] = A_list[i]
    stack.append(i)

print(*result)