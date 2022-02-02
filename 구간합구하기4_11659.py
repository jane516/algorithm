import sys

N, M = map(int, input().split())
case = sys.stdin.readline().strip().split()
A = [0] * (N + 1)
A[0] = 0
for i in range(1, N + 1):
    A[i] = int(case[i-1]) + A[i-1]
for i in range(M):
    case2 = sys.stdin.readline().strip().split()
    a = int(case2[0])
    b = int(case2[1])
    print(A[b] - A[a-1])
