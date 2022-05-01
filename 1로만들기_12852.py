from collections import deque
N = int(input())
if N == 1:
    print(0)
    print(1)
else:
    dp = [0] * (N + 1)
    queue = deque()
    queue.append((1, [1]))
    while queue:
        X, Y = queue.popleft()
        dx = [X + 1, 2 * X, 3 * X]
        for nx in dx:
            if nx <= N and dp[nx] == 0:
                if nx == N:
                    print(dp[X] + 1)
                    result = Y + [nx]
                    print(*result[::-1])
                queue.append((nx, Y + [nx]))
                dp[nx] = dp[X] + 1
