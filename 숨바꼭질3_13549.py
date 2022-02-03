from collections import deque

N, K = map(int, input().split())
visited = [-1 for _ in range(200001)]
visited[N] = 0

queue = deque([N])
while queue:
    X = queue.popleft()
    if X == K:
        break

    if 0 <= 2 * X <= 200000:
        if visited[2 * X] == -1:
            visited[2 * X] = visited[X]
            queue.append(2 * X)
    이동 = [X - 1, X + 1]
    for i in 이동:
        if 0 <= i <= 200000:
            if visited[i] == -1:
                visited[i] = visited[X] + 1
                queue.append(i)
print(visited[K])