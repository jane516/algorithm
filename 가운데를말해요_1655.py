import heapq
import sys
N = int(sys.stdin.readline().strip())
heap = []
for i in range(N):
    n = int(sys.stdin.readline().strip())
    heapq.heappush(heap, n)
    heap.sort()
    if len(heap) % 2 == 1:
        print(heap[len(heap) // 2])
    else:
        print(heap[len(heap) // 2 - 1])