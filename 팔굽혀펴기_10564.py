import sys
T = int(input())
for i in range(T):
    N, M = map(int, input().split())
    case = sys.stdin.readline().strip().split()
    score = []
    for j in range(M):
        score.append(int(case[j]))
