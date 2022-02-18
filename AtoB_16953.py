import sys
from collections import deque
case = sys.stdin.readline().strip().split()
A, B = int(case[0]), int(case[1])
visited = []
queue = deque([A])
check = 0
while queue:
    X = queue.popleft()
    k = 0
    if X > B:
        check = 1
        break
    if X == B:
        print(visited[1])
        break
    dX = [2 * X, 10 * X + 1]
    for i in dX:
        if i <= B:
            if i not in visited:
                k += 1
                visited.append([i, k])
                queue.append(i)
if B not in visited:
    print(-1)



