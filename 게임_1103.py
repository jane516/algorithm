import sys
N, M = map(int, input().split())
board = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip()
    for j in range(M):
        board[i][j] = case[j]
visited = [[0 for _ in range(M)] for _ in range(N)]
dp = [[0 for _ in range(M)] for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
result = 0


def dfs(x, y, cnt):
    global result
    result = max(result, cnt)
    for i in range(4):
        nx = x + dx[i] * int(board[x][y])
        ny = y + dy[i] * int(board[x][y])
        if 0 <= nx < N and 0 <= ny < M and board[nx][ny] != 'H' and cnt + 1 > dp[nx][ny]:
            if visited[nx][ny]:
                print(-1)
                exit()
            else:
                dp[nx][ny] = cnt + 1
                visited[nx][ny] = 1
                dfs(nx, ny, cnt + 1)
                visited[nx][ny] = 0


dfs(0, 0, 0)
print(result + 1)