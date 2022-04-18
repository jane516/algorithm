import sys
N, M = map(int, sys.stdin.readline().strip().split())
num_list = [[0 for _ in range(N)] for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    for j in range(N):
        num_list[i][j] = int(case[j])
my_list = [[0 for _ in range(N + 1)] for _ in range(N)]
for i in range(N):
    for j in range(1, N + 1):
        my_list[i][j] = my_list[i][j-1] + num_list[i][j-1]
result = []
for i in range(M):
    case2 = sys.stdin.readline().strip().split()
    Sum = 0
    x1, y1, x2, y2 = int(case2[0]), int(case2[1]), int(case2[2]), int(case2[3])
    for j in range(x1 - 1, x2):
        Sum += my_list[j][y2] - my_list[j][y1-1]
    result.append(Sum)
for i in range(M):
    print(result[i])