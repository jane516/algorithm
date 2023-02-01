import sys

N, M = map(int, sys.stdin.readline().strip().split())

board = [["" for _ in range(M)] for _ in range(N)]

for i in range(N):
    _str = sys.stdin.readline().strip()
    for j in range(M):
        board[i][j] = _str[j]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = [[2 for _ in range(M)] for _ in range(N)]

for i in range(N):
    for j in range(M):
        for k in range(4):
            X = j + dx[k]
            Y = i + dy[k]
            if Y < 0 or Y >= N:
                continue
            if X < 0 or X >= M:
                continue
            if board[Y][X] == 'W':
                board[Y][X] = 'B'
            else:
                board[Y][X] = 'W'

for i in range(N):
    for j in range(M):
        if board[i][j] == 'B':
            result[i][j] = 3

print(1)
for i in range(N):
    for j in range(M):
        if j == M - 1:
            print(result[i][j])
        else:
            print(result[i][j], end='')