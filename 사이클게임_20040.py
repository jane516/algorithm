import sys
n, m = map(int, sys.stdin.readline().strip().split())
visited = {i: i for i in range(n + 1)}
link = [list(map(int, sys.stdin.readline().strip().split())) for _ in range(m)]
check = 0


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


for i, node in enumerate(link):
    a, b = node[0], node[1]
    if find(a) != find(b):
        union(a, b)
    else:
        print(i + 1)
        check = 1
        break
if check == 0:
    print(0)