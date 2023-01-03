import sys

N = int(sys.stdin.readline().strip())
area = [[0 for _ in range(N)] for _ in range(N)]
Max_h = 0
result = 0

for i in range(N):
    area[i] = list(map(int, sys.stdin.readline().strip().split()))
    for M in area[i]:
        Max_h = max(Max_h, M)

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for height in range(Max_h):
    stack = []
    visited = [[0 for _ in range(N)] for _ in range(N)]

    Sum = 0

    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0 and area[i][j] > height:
                stack.append((i, j))
                Sum += 1
                visited[i][j] = 1
                while stack:
                    D = stack.pop()
                    for k in range(4):
                        x = D[0] + dx[k]
                        y = D[1] + dy[k]
                        if x < 0 or y < 0 or x >= N or y >= N:
                            continue
                        if visited[x][y] == 1 or area[x][y] <= height:
                            continue
                        visited[x][y] = 1
                        stack.append((x, y))

    result = max(result, Sum)

print(result)