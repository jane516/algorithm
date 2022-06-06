import sys
N, M = map(int, input().split())
Matrix = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    Str = sys.stdin.readline().strip()
    for j in range(M):
        Matrix[i][j] = int(Str[j])
sol = -1


def 제곱수(n):
    x = int(n ** 0.5)
    if x ** 2 == n:
        return 1
    else:
        return 0


for x_start in range(N):
    for y_start in range(M):
        for dx in range(-N, N):
            for dy in range(-M, M):
                if dx == 0 and dy == 0:
                    continue
                x = x_start
                y = y_start
                step = 0
                result = ''
                while (0 <= x < N) and (0 <= y < M):
                    result += str(Matrix[x][y])
                    step += 1

                    X = int(''.join(result))
                    if 제곱수(X) == 1 and X > sol:
                        sol = X
                    x = x_start + step * dx
                    y = y_start + step * dy
print(sol)


