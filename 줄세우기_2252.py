import sys
from collections import deque
N, M = map(int, sys.stdin.readline().strip().split())
link = [[] for _ in range(N)]
count = [0 for _ in range(N)]
result = []
queue = deque()
for _ in range(M):
    start, end = map(int, sys.stdin.readline().strip().split())
    link[start - 1].append(end - 1)
    count[end - 1] += 1
for i in range(N):
    if count[i] == 0:
        result.append(i + 1)
        queue.append(i)
while queue:
    X = queue.popleft()
    for j in link[X]:
        count[j] -= 1
        if count[j] == 0:
            queue.append(j)
            result.append(j + 1)
print(*result)

