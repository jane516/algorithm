import sys
from collections import deque

T = int(input())
for _ in range(T):
    N, K = map(int, sys.stdin.readline().strip().split())
    time = list(map(int, sys.stdin.readline().strip().split()))
    link = [[] for _ in range(N)]
    count = [0 for _ in range(N)]
    for _ in range(K):
        start, end = map(int, sys.stdin.readline().strip().split())
        link[start-1].append(end-1)
        count[end-1] += 1
    W = int(input())
    queue = deque()
    dp = [0 for _ in range(N)]
    for i in range(N):
        if count[i] == 0:
            queue.append(i)
            dp[i] = time[i]
    while queue:
        X = queue.popleft()
        for i in link[X]:
            count[i] -= 1
            dp[i] = max(dp[i], dp[X] + time[i])
            if count[i] == 0:
                queue.append(i)
        if count[W - 1] == 0:
            print(dp[W-1])
            break


