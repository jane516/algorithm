import sys
N = int(input())
case = sys.stdin.readline().strip().split()
A = [0 for _ in range(N)]
for i in range(N):
    A[i] = int(case[i])
H = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    for j in range(N):
        if i == j:
            H[i][j] = 0
        else:
            H[i][j] = (A[i] - A[j]) / (i - j)
my_list = [0 for _ in range(N)]
for i in range(N):
    Sum1 = 0
    Sum2 = 0
    for j in range(i):
        DP = [1 for _ in range(N)]
        for k in range(i):
            for l in range(k):
                if H[i][k] < H[i][l]:
                    DP[k] = max(DP[k], DP[l] + 1)
        Sum1 = max(DP)
    for j in range(i, N):
        DP = [1 for _ in range(N)]
        for k in range(i, N):
            for l in range(i, k):
                if H[i][k] > H[i][l]:
                    DP[k] = max(DP[k], DP[l] + 1)
        Sum2 = max(DP)
    my_list[i] = Sum1 + Sum2
print(max(my_list))
