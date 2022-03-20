import heapq
import sys
T = int(sys.stdin.readline().strip())
for i in range(T):
    min_heap = []
    max_heap = []
    k = int(sys.stdin.readline().strip())
    visited = [0 for _ in range(k)]
    for j in range(k):
        case = sys.stdin.readline().strip().split()
        if case[0] == 'I':
            x = int(case[1])
            heapq.heappush(min_heap, (x, j))
            heapq.heappush(max_heap, (-x, j))
            visited[j] = 1
        else:
            if case[1] == '-1':
                while min_heap and not visited[min_heap[0][1]]:
                        heapq.heappop(min_heap)
                if min_heap:
                    visited[min_heap[0][1]] = 0
                    heapq.heappop(min_heap)
            else:
                while max_heap and not visited[max_heap[0][1]]:
                    heapq.heappop(max_heap)
                if max_heap:
                    visited[max_heap[0][1]] = 0
                    heapq.heappop(max_heap)
    while min_heap and not visited[min_heap[0][1]]:
        heapq.heappop(min_heap)
    while max_heap and not visited[max_heap[0][1]]:
        heapq.heappop(max_heap)
    if min_heap:
        print(-max_heap[0][0], min_heap[0][0])
    else:
        print('EMPTY')

