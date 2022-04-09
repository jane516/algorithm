import sys
N = int(input())
case = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
result = [[0 for _ in range(N)] for _ in range(N)]
visited = [[0 for _ in range(N)] for _ in range(N)]


def palindrome(a, b):
    x, y = a-1, b-1
    visited[a-1][b-1] = 1
    check = 1
    while x < y:
        if case[x] != case[y]:
            check = 0
            break
        x += 1
        y -= 1
    result[a-1][b-1] = check


for i in range(M):
    case2 = sys.stdin.readline().strip().split()
    a, b = int(case2[0]), int(case2[1])
    if visited[a-1][b-1]:
        print(result[a-1][b-1])
    else:
        palindrome(a, b)
        print(result[a-1][b-1])