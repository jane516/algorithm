def DFS(x):
    global count
    if x == N:
        count += 1
        return

    for i in range(N):
        visited[x] = i
        if check(x):
            DFS(x + 1)


def check(x):
    for i in range(x):
        if visited[x] == visited[i] or abs(visited[x] - visited[i]) == x - i:
            return False
    return True


N = int(input())
visited = [0] * N
count = 0
DFS(0)
print(count)