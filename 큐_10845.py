import sys
from collections import deque

N = int(input())
queue = deque([])
for i in range(N):
    case = sys.stdin.readline().strip()
    a = case.split(" ")[0]
    if a == 'push':
        b = int(case.split(" ")[1])
        queue.append(b)
    if a == 'pop':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
            queue.popleft()
    if a == 'size':
        print(len(queue))
    if a == 'empty':
        if len(queue) == 0:
            print(1)
        else:
            print(0)
    if a == 'front':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[0])
    if a == 'back':
        if len(queue) == 0:
            print(-1)
        else:
            print(queue[-1])