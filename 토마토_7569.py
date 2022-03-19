import sys
from collections import deque
M, N, H = map(int, input().split())
queue = deque([])
result = 0
tomato = [[[0 for _ in range(M)] for _ in range(N)] for _ in range(H)]
for i in range(H):
    for j in range(N):
        case = sys.stdin.readline().strip().split()
        for k in range(M):
            tomato[i][j][k] = int(case[k])
dx, dy, dz = [-1, 1, 0, 0, 0, 0], [0, 0, -1, 1, 0, 0], [0, 0, 0, 0, -1, 1]
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 1:
                queue.append([i, j, k])


def bfs():
    while queue:
        x, y, z = queue.popleft()
        for i in range(6):
            nx, ny, nz = dx[i] + x, dy[i] + y, dz[i] + z
            if 0 <= nx < H and 0 <= ny < N and 0 <= nz < M and tomato[nx][ny][nz] == 0:
                tomato[nx][ny][nz] = tomato[x][y][z] + 1
                queue.append([nx, ny, nz])


bfs()
for i in range(H):
    for j in range(N):
        for k in range(M):
            if tomato[i][j][k] == 0:
                print(-1)
                exit(0)
            result = max(result, tomato[i][j][k])
print(result-1)