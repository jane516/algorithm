import sys
from collections import deque
N, M = map(int, input().split())
N_list = [i for i in range(1, N + 1)]
out_list = list(map(int, sys.stdin.readline().strip().split()))
cnt = 0
queue = deque(N_list)
for i in range(M):
    idx = queue.index(out_list[i])
    if idx < len(queue) / 2:
        while True:
            if queue[0] == out_list[i]:
                queue.popleft()
                break
            X = queue.popleft()
            queue.append(X)
            cnt += 1
    else:
        while True:
            if queue[0] == out_list[i]:
                queue.popleft()
                break
            X = queue.pop()
            queue.appendleft(X)
            cnt += 1
print(cnt)
