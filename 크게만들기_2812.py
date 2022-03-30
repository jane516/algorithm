import sys
from collections import deque
case = sys.stdin.readline().strip().split()
N, K = int(case[0]), int(case[1])
number = list(map(int, sys.stdin.readline().strip()))
queue = deque(number)
count = 0
result = [0]
while queue:
    if count == K + 1:
        while queue:
            Y = queue.popleft()
            result.append(Y)
        break
    X = queue.popleft()
    if result[-1] < X:
        while result:
            if result[-1] >= X:
                break
            result.pop()
            count += 1
            if count == K + 1:
                break
        result.append(X)
    elif result[-1] == X:
        result.append(X)
    else:
        result.append(X)
for i in range(N - K):
    print(result[i], end='')