import sys


def DFS(N, M, s, j):
    if len(s) == M:
        my_list.append(list(s))
        return
    for i in range(j, N):
        if visited[i]:
            s.append(A[i])
            DFS(N, M, s, i)
            s.pop()
            visited[i] = False
            continue
        visited[i] = True
        s.append(A[i])
        DFS(N, M, s, i)
        s.pop()
        visited[i] = False


N, M = map(int, input().split())
case = sys.stdin.readline().strip().split()
A = []
my_list = []
visited = [False] * N
s = []
for i in range(N):
    A.append(int(case[i]))
A.sort()
DFS(N, M, s, 0)
result = []
for i in range(len(my_list)):
    t = tuple(my_list[i])
    result.append(t)
B = sorted(set(result))
for i in B:
    print(*i)
