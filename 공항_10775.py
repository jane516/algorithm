import sys
from collections import deque
G = int(sys.stdin.readline().strip())
P = int(sys.stdin.readline().strip())
visited = {i: 0 for i in range(1, G + 1)}
stack = deque([])
M = 0
count = 0
for i in range(P):
    g = int(sys.stdin.readline().strip())
    stack.append(g)

while stack:
    X = stack.popleft()
    count += 1
    for i in range(X, G + 1):
        visited[i] += 1
        if visited[i] > i:
            print(count - 1)
            sys.exit(0)
