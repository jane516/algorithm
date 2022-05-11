import sys
T = int(input())
for _ in range(T):
    h, w = map(int, input().split())
    building = [[0 for _ in range(w)] for _ in range(h)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    start = []
    for i in range(h):
        case = list(sys.stdin.readline().strip())
        for j in range(w):
            a = case[j]
            building[i][j] = a
            if i == 0 or i == h - 1:
                if a == '.':
                    start.append([i, j])
            elif j == 0 or j == w - 1:
                if a == '.':
                    start.append([i, j])
    key = list(sys.stdin.readline().strip())
