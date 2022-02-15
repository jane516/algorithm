import sys
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    case = sys.stdin.readline().strip().split()
    score = []
    for j in range(M):
        score.append(int(case[j]))
    DP = [[0 for _ in range(500)] for _ in range(5001)]

    for i in range():
        for j in range():
            for k in score:
                if i - j >= 0 and j - k >= 0:
                    DP[i][j] = max(DP[i][j], DP[i - j][j - k] + k)

    print(max(DP[N]))
