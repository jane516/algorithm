import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
board = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    L = list(map(int, sys.stdin.readline().strip()))
    for j in range(m):
        board[i][j] = L[j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for _ in range(m)] for _ in range(n)]

queue = deque([(0, 0)])

while queue:
    D = queue.popleft()
    for k in range(4):
        x = D[0] + dx[k]
        y = D[1] + dy[k]
        if x < 0 or y < 0 or x >= n or y >= m:
            continue
        if visited[x][y] == 1 or board[x][y] == 0:
            continue
        board[x][y] = board[D[0]][D[1]] + 1
        queue.append((x, y))

print(board[n-1][m-1])

