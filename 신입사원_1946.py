import sys
T = int(input())
for i in range(T):
    N = int(sys.stdin.readline().strip())
    성적표 = [[0 for _ in range(2)] for _ in range(N)]
    for j in range(N):
        case = sys.stdin.readline().strip().split()
        성적표[j][0], 성적표[j][1] = int(case[0]), int(case[1])
    성적표.sort()
    count = 1
    min = 성적표[0][1]
    for j in range(1, N):
        if 성적표[j][1] < min:
            count += 1
            min = 성적표[j][1]
    print(count)