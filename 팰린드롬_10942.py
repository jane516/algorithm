import sys
N = int(input())
case = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
result = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    result[i][i] = 1
    if i != N - 1:
        if case[i] == case[i + 1]:
            result[i][i+1] = 1


def palindrome(a, b):
    x, y = a-1, b-1
    check = 1
    while x < y:
        if case[x] != case[y]:
            check = 0
            break
        if visited[x][y] == 1:
            check = result[x][y]
            break
        x += 1
        y -= 1
    result[a - 1][b - 1] = check
    visited[a - 1][b - 1] = 1


for i in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    if visited[a-1][b-1]:
        print(result[a-1][b-1])
    else:
        palindrome(a, b)
        print(result[a-1][b-1])