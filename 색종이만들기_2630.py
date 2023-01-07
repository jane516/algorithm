import sys

N = int(sys.stdin.readline().strip())
Matrix = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    Matrix[i] = list(map(int, sys.stdin.readline().strip().split()))

result = [0, 0]


def solve(x, y, n):
    global result
    num = Matrix[x][y]

    for i in range(x, x + n):
        for j in range(y, y + n):
            if Matrix[i][j] != num:
                for k in range(2):
                    for l in range(2):
                        solve(x + k * n // 2, y + l * n // 2, n // 2)
                return
    if num == 0:
        result[0] += 1
    else:
        result[1] += 1


solve(0, 0, N)
print(result[0])
print(result[1])