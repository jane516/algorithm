from collections import deque

N, M, V = map(int, input().split())
node = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(M):
    n1, n2 = map(int, input().split())
    node[n1][n2] = 1
    node[n2][n1] = 1


def DFS(first):
    stack = [first]
    result = []
    visited = [False] * (N+1)

    while stack:
        top = stack.pop()
        if visited[top]:
            continue

        result.append(str(top))
        visited[top] = True
        for idx, linked in enumerate(list(reversed(node[top][1:]))):
            if linked == 1 and not visited[N-idx]:
                stack.append(N-idx)

    return result


def BFS(first):
    queue = deque([first])
    result = []
    visited = [False] * (N+1)

    while queue:
        top = queue.popleft()
        if visited[top]:
            continue

        result.append(str(top))
        visited[top] = True
        for idx, linked in enumerate(node[top][1:]):
            if linked == 1 and not visited[idx+1]:
                queue.append(idx+1)
    return result


print(' '.join(DFS(V)))
print(' '.join(BFS(V)))