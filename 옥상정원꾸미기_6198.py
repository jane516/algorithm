import sys

N = int(sys.stdin.readline().strip())
A_list = [0 for _ in range(N)]

for i in range(N):
    A_list[i] = int(sys.stdin.readline().strip())
stack = []
result = 0

for i in range(N):
    while stack and A_list[stack[-1]] < A_list[N - 1 - i]:
        result += 1
        stack.pop()
    stack.append(N - 1 - i)

if len(A_list) > 1 and A_list[0] > A_list[1]:
    result += 1
print(result)