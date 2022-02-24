from collections import deque
import sys
N = int(input())
queue = deque()
for i in range(N):
    case = sys.stdin.readline().strip().split()
    if case[0] == 'push_front':
        queue.appendleft(int(case[1]))
    elif case[0] == 'push_back':
        queue.append(int(case[1]))
    elif case[0] == 'pop_front':
        if queue:
            X = queue.popleft()
            print(X)
        else:
            print(-1)
    elif case[0] == 'pop_back':
        if queue:
            X = queue.pop()
            print(X)
        else:
            print(-1)
    elif case[0] == 'size':
        print(len(queue))
    elif case[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)
    elif case[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)
    elif case[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)