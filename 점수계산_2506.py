import sys
N = int(input())
OX = [0 for _ in range(N)]
score = [0 for _ in range(N)]
case = sys.stdin.readline().strip().split()
for i in range(N):
    OX[i] = int(case[i])
score[0] = OX[0]
for i in range(1, N):
    if OX[i] == 0:
        score[i] = 0
    else:
        if OX[i-1] == 0:
            score[i] = 1
        else:
            score[i] = score[i-1] + 1
print(sum(score))