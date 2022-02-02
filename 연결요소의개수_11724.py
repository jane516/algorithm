def DFS(first, visited):
    stack = [first]
    result = []

    while stack:
        top = stack.pop()
        if visited[top]:
            continue

        result.append(str(top))
        visited[top] = True
        for idx, linked in enumerate(list(reversed(nodes[top][1:]))):
            if linked == 1 and not visited[N-idx]:
                stack.append(N-idx)
    return result


N, M = map(int, input().split())
nodes = [[0 for _ in range(N+1)] for _ in range(N+1)]
visited = [False] * (N+1)
for i in range(M):
    u, v = map(int, input().split())
    nodes[u][v] = 1
    nodes[v][u] = 1
count = 0
for i in range(1, N+1):
    if len(DFS(i, visited)):
        count += 1
print(count)