import sys
from collections import deque
M, N, H = map(int, input().split())
queue = deque([])
result = 0
tomato = [[0 for _ in range(M)] for _ in range(N * H)]
for i in range(N * H):
    case = sys.stdin.readline().strip().split()
    for j in range(M):
        tomato[i][j] = int(case[j])
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
for i in range(N * H):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            for j in range(H):
                if j * N <= nx < (j + 1) * N and 0 <= ny < M and tomato[nx][ny] == 0:
                    tomato[nx][ny] = tomato[x][y] + 1
                    queue.append([nx, ny])
                if (j + 1) * N <= x + N < (j + 2) * N and x + N < N * H:
                    if tomato[x + N][y] == 0:
                        tomato[x + N][y] = tomato[x][y] + 1
                        queue.append([x + N, y])
                if (j - 1) * N <= x - N < j * N and x - N >= 0:
                    if tomato[x - N][y] == 0:
                        tomato[x - N][y] = tomato[x][y] + 1
                        queue.append([x - N, y])


bfs()
for i in range(N * H):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, tomato[i][j])
print(result-1)