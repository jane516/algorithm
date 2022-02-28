import sys
N, M = map(int, input().split())
square = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip()
    for j in range(M):
        square[i][j] = case[j]
result = []
check = 0
for i in range(N-1):
    for j in range(M-1):
        for k in range(1, min(N, M)):
            if i + k < N and j + k < M:
                if square[i][j] == square[i][j+k]:
                    if square[i+k][j] == square[i][j]:
                        if square[i+k][j+k] == square[i][j]:
                            check = 1
                            result.append((k+1) ** 2)
if check == 0:
    print(1)
else:
    print(max(result))