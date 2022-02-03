from collections import deque

N, K = map(int, input().split())
visited = [0 for _ in range(200000)]


count = 0
queue = deque([N])
while queue:
    X = queue.popleft()
    if X == K:
        count = queue.count(K)
        break
    이동 = [X - 1, X + 1, 2 * X]
    for i in 이동:
        if 0 <= i < 200000:
            if not visited[i] or visited[i] >= visited[X] + 1:
                visited[i] = visited[X] + 1
                queue.append(i)
print(visited[K])
print(count + 1)
