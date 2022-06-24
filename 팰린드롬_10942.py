import sys
N = int(input())
case = list(map(int, sys.stdin.readline().strip().split()))
M = int(sys.stdin.readline().strip())
result = [[0 for _ in range(N)] for _ in range(N)]

for i in range(N):
    for j in range(N - i):
        k = j + i
        if j == k:
            result[j][k] = 1
        elif k - j == 1:
            if case[j] == case[k]:
                result[j][k] = 1
        else:
            if result[j + 1][k - 1] == 1 and case[j] == case[k]:
                result[j][k] = 1
for _ in range(M):
    a, b = map(int, sys.stdin.readline().strip().split())
    print(result[a - 1][b - 1])