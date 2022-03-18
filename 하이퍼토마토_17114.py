import sys
from collections import deque
m, n, o, p, q, r, s, t, u, v, w = map(int, input().split())
queue = deque([])
result = 0
tomato = [[[[[[[[[[[0 for _ in range(m)] for _ in range(n)]
          for _ in range(o)] for _ in range(p)] for _ in range(q)]
            for _ in range(r)] for _ in range(s)] for _ in range(t)]
            for _ in range(u)] for _ in range(v)] for _ in range(w)]
for a in range(w):
    for b in range(v):
        for c in range(u):
            for d in range(t):
                for e in range(s):
                    for f in range(r):
                        for g in range(q):
                            for h in range(p):
                                for i in range(o):
                                    for j in range(n):
                                        case = sys.stdin.readline().strip().split()
                                        for k in range(m):
                                            tomato[a][b][c][d][e][f][g][h][i][j][k] = int(case[k])
d1 = [-1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d2 = [0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d3 = [0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d4 = [0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d5 = [0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d6 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
d7 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0, 0, 0]
d8 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0, 0, 0]
d9 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0, 0, 0]
d10 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1, 0, 0]
d11 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, -1, 1]

for a in range(w):
    for b in range(v):
        for c in range(u):
            for d in range(t):
                for e in range(s):
                    for f in range(r):
                        for g in range(q):
                            for h in range(p):
                                for i in range(o):
                                    for j in range(n):
                                        for k in range(m):
                                            if tomato[a][b][c][d][e][f][g][h][i][j][k] == 1:
                                                queue.append([a, b, c, d, e, f, g, h, i, j, k])


def bfs():
    while queue:
        a, b, c, d, e, f, g, h, i, j, k = queue.popleft()
        for x in range(22):
            n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11 = d1[x] + a, d2[x] + b, d3[x] + c, d4[x] + d, \
                                                           d5[x] + e, d6[x] + f, d7[x] + g, d8[x] + h, \
                                                           d9[x] + i, d10[x] + j, d11[x] + k
            if 0 <= n1 < w and 0 <= n2 < v and 0 <= n3 < u and 0 <= n4 < t \
                    and 0 <= n5 < s and 0 <= n6 < r and 0 <= n7 < q and 0 <= n8 < p \
                    and 0 <= n9 < o and 0 <= n10 < n and 0 <= n11 < m \
                    and tomato[n1][n2][n3][n4][n5][n6][n7][n8][n9][n10][n11] == 0:
                tomato[n1][n2][n3][n4][n5][n6][n7][n8][n9][n10][n11] = tomato[a][b][c][d][e][f][g][h][i][j][k] + 1
                queue.append([n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11])


bfs()
for a in range(w):
    for b in range(v):
        for c in range(u):
            for d in range(t):
                for e in range(s):
                    for f in range(r):
                        for g in range(q):
                            for h in range(p):
                                for i in range(o):
                                    for j in range(n):
                                        for k in range(m):
                                            if tomato[a][b][c][d][e][f][g][h][i][j][k] == 0:
                                                print(-1)
                                                exit(0)
                                            result = max(result, tomato[a][b][c][d][e][f][g][h][i][j][k])
print(result-1)