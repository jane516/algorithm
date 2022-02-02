import sys
from collections import deque

T = int(input())
for i in range(T):
    case = list(sys.stdin.readline().strip())
    n = int(input())
    A = deque(sys.stdin.readline().strip()[1:-1].split(","))
    if n == 0:
        A = deque()
    R_count = 0
    Check = 0
    for j in case:
        if j == 'R':
            R_count += 1
        else:
            if len(A) == 0:
                Check = 1
                break
            else:
                if R_count % 2 == 0:
                    A.popleft()
                else:
                    A.pop()
    if Check == 1:
        print('error')
    else:
        print('[', end='')
        if R_count % 2 == 1:
            A.reverse()
        for k in range(len(A)):
            print(A[k], end='')
            if len(A) != 0:
                if k != len(A) - 1:
                    print(',', end='')
        print(']')

