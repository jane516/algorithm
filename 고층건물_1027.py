import sys

N = int(input())
case = sys.stdin.readline().strip().split()
A = [0 for _ in range(N)]
for i in range(N):
    A[i] = int(case[i])
H = [[0 for _ in range(N+1)] for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        if i == j:
            H[i][j] = 0
        else:
            H[i][j] = (A[i-1] - A[j-1]) / (i - j)
my_list = [1 for _ in range(N+1)]
for i in range(1, N + 1):
    if N == 1:
        print(0)
        exit(0)
    Sum1 = 1
    Sum2 = 1
    if i == 1:
        Max = H[i][i + 1]
        for j in range(i+1, N+1):
            if H[i][j] > Max:
                my_list[i] += 1
                Max = H[i][j]
    elif i == N:
        Min = H[i][i - 1]
        for j in range(i - 1, -1, -1):
            if H[i][j] < Min:
                my_list[i] += 1
                Min = H[i][j]
            if j == 1:
                if H[i][j] < Min:
                    my_list[i] += 1
                break

    else:
        Min = H[i][i - 1]
        for j in range(i-1, -1, -1):
            if H[i][j] < Min:
                Sum1 += 1
                Min = H[i][j]
            if j == 1:
                if H[i][j] < Min:
                    Sum1 += 1
                break

        Max = H[i][i + 1]
        for j in range(i+1, N+1):
            if H[i][j] > Max:
                Sum2 += 1
                Max = H[i][j]
        my_list[i] = Sum1 + Sum2

print(max(my_list))

