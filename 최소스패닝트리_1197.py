import sys
import heapq
V, E = map(int, sys.stdin.readline().strip().split())
visited = [0 for _ in range(V + 1)]
Elist = [[] for _ in range(V + 1)]
heap = [[0, 1]]
for _ in range(E):
    A, B, C = map(int, sys.stdin.readline().strip().split())
    Elist[A].append([C, B])
    Elist[B].append([C, A])
answer, count = 0, 0
while heap:
    if count == V:
        break
    C, A = heapq.heappop(heap)
    if not visited[A]:
        visited[A] = 1
        answer += C
        count += 1
        for i in Elist[A]:
            heapq.heappush(heap, i)
print(answer)