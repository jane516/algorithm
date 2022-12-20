import sys
from collections import deque

n = int(sys.stdin.readline().strip())
board1 = [[0 for _ in range(n)] for _ in range(n)]
board2 = [[0 for _ in range(n)] for _ in range(n)]

for i in range(n):
    List = sys.stdin.readline().strip()
    for j in range(n):
        board1[i][j] = List[j]
        if List[j] != 'R':
            board2[i][j] = List[j]
        else:
            board2[i][j] = 'G'

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

visited = [[0 for _ in range(n)] for _ in range(n)]

queue1 = deque([])
queue2 = deque([])
queue3 = deque([])

Sum1 = 0

for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and board1[i][j] == 'G':
            queue1.append((i, j))
            Sum1 += 1
            visited[i][j] = 1
            while queue1:
                D = queue1.popleft()
                for k in range(4):
                    x = D[0] + dx[k]
                    y = D[1] + dy[k]
                    if x < 0 or y < 0 or x >= n or y >= n:
                        continue
                    if visited[x][y] == 1 or board1[x][y] != 'G':
                        continue
                    visited[x][y] = 1
                    queue1.append((x, y))
        if visited[i][j] == 0 and board1[i][j] == 'B':
            queue2.append((i, j))
            Sum1 += 1
            visited[i][j] = 1
            while queue2:
                D = queue2.popleft()
                for k in range(4):
                    x = D[0] + dx[k]
                    y = D[1] + dy[k]
                    if x < 0 or y < 0 or x >= n or y >= n:
                        continue
                    if visited[x][y] == 1 or board1[x][y] != 'B':
                        continue
                    visited[x][y] = 1
                    queue2.append((x, y))
        if visited[i][j] == 0 and board1[i][j] == 'R':
            queue3.append((i, j))
            Sum1 += 1
            visited[i][j] = 1
            while queue3:
                D = queue3.popleft()
                for k in range(4):
                    x = D[0] + dx[k]
                    y = D[1] + dy[k]
                    if x < 0 or y < 0 or x >= n or y >= n:
                        continue
                    if visited[x][y] == 1 or board1[x][y] != 'R':
                        continue
                    visited[x][y] = 1
                    queue3.append((x, y))

visited = [[0 for _ in range(n)] for _ in range(n)]

queue1 = deque([])
queue2 = deque([])

Sum = 0


for i in range(n):
    for j in range(n):
        if visited[i][j] == 0 and board2[i][j] == 'G':
            queue1.append((i, j))
            Sum += 1
            visited[i][j] = 1
            while queue1:
                D = queue1.popleft()
                for k in range(4):
                    x = D[0] + dx[k]
                    y = D[1] + dy[k]
                    if x < 0 or y < 0 or x >= n or y >= n:
                        continue
                    if visited[x][y] == 1 or board2[x][y] == 'B':
                        continue
                    visited[x][y] = 1
                    queue1.append((x, y))
        if visited[i][j] == 0 and board2[i][j] == 'B':
            queue2.append((i, j))
            Sum += 1
            visited[i][j] = 1
            while queue2:
                D = queue2.popleft()
                for k in range(4):
                    x = D[0] + dx[k]
                    y = D[1] + dy[k]
                    if x < 0 or y < 0 or x >= n or y >= n:
                        continue
                    if visited[x][y] == 1 or board2[x][y] == 'G':
                        continue
                    visited[x][y] = 1
                    queue2.append((x, y))
print(Sum1, Sum)