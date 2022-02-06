from collections import deque

N, M = map(int, input().split())
A = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    case = list(input())
    for j in range(M):
        A[i][j] = int(case[j])

queue = deque([[0, 0]])

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

while queue:
    x, y = queue[0][0], queue[0][1]

    queue.popleft()
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and ny >= 0 and nx < N and ny < M:
            if A[nx][ny] == 1:
                queue.append([nx, ny])
                A[nx][ny] = A[x][y] + 1
print(A[N-1][M-1])