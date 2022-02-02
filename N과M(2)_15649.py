def DFS(N, M, s, j):
    if len(s) == M:
        print(*s)
        return

    for i in range(j, N+1):
        if visited[i]:
            continue

        visited[i] = True
        s.append(i)
        DFS(N, M, s, i + 1)
        s.pop()
        visited[i] = False


N, M = map(int, input().split())
s = []
visited = [False] * (N + 1)
DFS(N, M, s, 1)