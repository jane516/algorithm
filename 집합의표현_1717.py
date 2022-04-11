import sys
sys.setrecursionlimit(10**6)
case1 = sys.stdin.readline().strip().split()
n, m = int(case1[0]), int(case1[1])
visited = {i: i for i in range(n + 1)}


def find(x):
    if visited[x] == x:
        return x
    p = find(visited[x])
    visited[x] = p
    return visited[x]


def union(x, y):
    x = find(x)
    y = find(y)
    if x < y:
        visited[y] = x
    else:
        visited[x] = y


for i in range(m):
    case2 = sys.stdin.readline().strip().split()
    order = int(case2[0])
    a, b = int(case2[1]), int(case2[2])
    if order == 0:
        union(a, b)
    else:
        if find(a) == find(b):
            print('YES')
        else:
            print('NO')