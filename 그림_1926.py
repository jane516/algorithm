import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
board = [[0 for _ in range(m)] for _ in range(n)]

for i in range(n):
    board[i] = list(map(int, sys.stdin.readline().strip().split()))
    for j in range(m):
        board[i][j] = board[i][j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for _ in range(m)] for _ in range(n)]

queue = deque([])

Max = 0
Sum = 0

for i in range(n):
    for j in range(m):
        if visited[i][j] == 0 and board[i][j] == 1:
            queue.append((i, j))
            Sum += 1
            cnt = 1
            visited[i][j] = 1
            while queue:
                D = queue.popleft()
                for k in range(4):
                    x = D[0] + dx[k]
                    y = D[1] + dy[k]
                    if x < 0 or y < 0 or x >= n or y >= m:
                        continue
                    if visited[x][y] == 1 or board[x][y] == 0:
                        continue
                    visited[x][y] = 1
                    cnt += 1
                    queue.append((x, y))
            Max = max(Max, cnt)

print(Sum)
print(Max)

