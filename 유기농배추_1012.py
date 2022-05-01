from collections import deque
T = int(input())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def BFS(graph, a, b):
    queue = deque()
    queue.append((a, b))
    graph[a][b] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return


for _ in range(T):
    M, N, K = map(int, input().split())
    locate = [[0 for _ in range(N)] for _ in range(M)]
    cnt = 0
    for i in range(K):
        X, Y = map(int, input().split())
        locate[X][Y] = 1
    for i in range(M):
        for j in range(N):
            if locate[i][j] == 1:
                BFS(locate, i, j)
                cnt += 1
    print(cnt)