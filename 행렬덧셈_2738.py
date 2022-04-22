import sys
N, M = map(int, input().split())
A = [[0 for _ in range(M)] for _ in range(N)]
B = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    for j in range(M):
        A[i][j] = int(case[j])
for i in range(N):
    case = sys.stdin.readline().strip().split()
    for j in range(M):
        B[i][j] = int(case[j])
C = [[0 for _ in range(M)] for _ in range(N)]
for i in range(N):
    for j in range(M):
        C[i][j] = A[i][j] + B[i][j]
    print(*C[i])
