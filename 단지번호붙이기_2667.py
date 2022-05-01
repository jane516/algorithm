from collections import deque
import sys
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    cnt = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
                cnt += 1
    return cnt


N = int(input())
locate = [[0 for _ in range(N)] for _ in range(N)]
cnt = 0
result = []
for i in range(N):
    case = list(sys.stdin.readline().strip())
    for j in range(N):
        locate[i][j] = int(case[j])
for i in range(N):
    for j in range(N):
        if locate[i][j] == 1:
            X = BFS(locate, i, j)
            result.append(X+1)
            cnt += 1
result.sort()
print(cnt)
for i in range(cnt):
    print(result[i])