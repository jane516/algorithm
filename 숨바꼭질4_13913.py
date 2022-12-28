import sys
from collections import deque

N, K = map(int, sys.stdin.readline().strip().split())
v_s = [-1 for _ in range(100001)]
v_s[N] = 0
queue = deque([(N, 0)])

while queue:
    X, t = queue.popleft()

    if X == K:
        print(t)
        arr = [X]
        while X != N:
            X = v_s[X]
            arr.append(X)
        print(*list(reversed(arr)))
        break
    dx = [X - 1, X + 1, 2 * X]

    for i in dx:
        if not 0 <= i <= 100000:
            continue
        if v_s[i] != -1:
            continue
        v_s[i] = X
        queue.append((i, t + 1))
