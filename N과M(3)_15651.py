def DFS(N, M, s):
    if len(s) == M:
        print(*s)
        return

    for i in range(1, N+1):
        if visited[i]:
            s.append(i)
            DFS(N, M, s)
            s.pop()
            visited[i] = False

        s.append(i)
        DFS(N, M, s)
        s.pop()
        visited[i] = False


N, M = map(int, input().split())
s = []
visited = [False] * (N+1)
DFS(N, M, s)