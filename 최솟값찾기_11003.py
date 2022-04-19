from collections import deque
import sys
case = sys.stdin.readline().strip().split()
N, L = int(case[0]), int(case[1])
my_list = list(map(int, sys.stdin.readline().strip().split()))
queue = deque()
for i in range(N):
    while queue and queue[-1][0] > my_list[i]:
        queue.pop()
    while queue and queue[0][1] < i - L + 1:
        queue.popleft()
    queue.append((my_list[i], i))
    print(queue[0][0], end = ' ')