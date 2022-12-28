import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
v_s = [[-1 for _ in range(500001)] for _ in range(2)]
v_s[0][N] = 0
queue = deque([(N, 0)])

while queue:
    X, t = queue.popleft()
    r = t % 2
    dx = [X - 1, X + 1, 2 * X]

    for i in dx:
        if not 0 <= i <= 500000:
            continue
        if v_s[1 - r][i] != -1:
            continue
        v_s[1 - r][i] = t + 1
        queue.append((i, t + 1))

time = 0
result = -1
while True:
    K = K + time
    if time > 1000 or K > 500000:
        break
    r = time % 2
    if -1 < v_s[r][K] <= time:
        result = time
        break
    time += 1

print(result)