N = int(input())
M = int(input())
node = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
for i in range(M):
    a, b = map(int, input().split())
    node[a][b], node[b][a] = 1, 1

stack = [1]
result = []
visited = [0] * (N + 1)
while stack:
    X = stack.pop()
    if visited[X]:
        continue
    result.append(X)
    visited[X] = 1
    for idx, linked in enumerate(list(reversed(node[X][1:]))):
        if linked == 1 and not visited[N - idx]:
            stack.append(N - idx)
print(len(result) - 1)