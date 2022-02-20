from collections import deque
N = int(input())
result = []
stack = deque([i for i in range(1, N + 1)])
while stack:
    result.append(stack.popleft())
    if not stack:
        break
    stack.append(stack[0])
    stack.popleft()
print(*result)