import sys
from collections import deque
M, N, H = map(int, input().split())
queue = deque([])
result = 0
tomato = [[[0 for _ in range(H)] for _ in range(M)] for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    for j in range(M):
        tomato[i][j] = int(case[j])
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 1:
            queue.append([i, j])


def bfs():
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx, ny = dx[i] + x, dy[i] + y
            if 0 <= nx < N and 0 <= ny < M and tomato[nx][ny] == 0:
                tomato[nx][ny] = tomato[x][y] + 1
                queue.append([nx, ny])


bfs()
for i in range(N):
    for j in range(M):
        if tomato[i][j] == 0:
            print(-1)
            exit(0)
        result = max(result, tomato[i][j])
print(result-1)