import sys
n = int(input())
a = [[0 for _ in range(6)] for _ in range(n)]
for i in range(n):
    case = sys.stdin.readline().strip().split()
    for j in range(6):
        a[i][j] = int(case[j])
