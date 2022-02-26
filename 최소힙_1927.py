import heapq
import sys
heap = []
N = int(sys.stdin.readline().strip())
for i in range(N):
    x = int(sys.stdin.readline().strip())
    if x == 0:
        if heap:
            result = heapq.heappop(heap)
            print(result)
        else:
            print(0)
    else:
        heapq.heappush(heap, x)