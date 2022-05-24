import sys
import heapq
N, K = map(int, input().split())
보석 = []
for _ in range(N):
    heapq.heappush(보석, list(map(int, sys.stdin.readline().strip().split())))
C_list = []
for _ in range(K):
    C_list.append(int(sys.stdin.readline().strip()))
C_list.sort()
result = 0
V_list = []
for i in C_list:
    while 보석 and i >= 보석[0][0]:
        heapq.heappush(V_list, -heapq.heappop(보석)[1])
    if V_list:
        result -= heapq.heappop(V_list)
    elif not 보석:
        break
print(result)
