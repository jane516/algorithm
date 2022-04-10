import sys
G = int(sys.stdin.readline().strip())
P = int(sys.stdin.readline().strip())
visited = {i: i for i in range(0, G + 1)}
plane = []
count = 0
for i in range(P):
    g = int(sys.stdin.readline().strip())
    plane.append(g)


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


for i in plane:
    x = find(i)
    if x == 0:
        break
    union(x, x-1)
    count += 1

print(count)
