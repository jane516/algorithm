import sys


def 두점거리(x1, y1, x2, y2):
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return d


N = int(input())
A = [[0 for _ in range(2)] for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    A[i][0] = int(case[0])
    A[i][1] = int(case[1])

B = [0] * N

for i in range(N):
    for j in range(N):
        l = 두점거리(A[i][0], A[i][1], A[j][0], A[j][1])
        if B[i] < l:
            B[i] = l
min = 10**4 * 2 * 2**0.5
result = 0
for i in range(N):
    if B[i] < min:
        result = i
        min = B[i]
print(A[result][0], A[result][1])
