import sys
N, L, H = map(int, input().split())
case = sys.stdin.readline().strip().split()
score = []
for i in range(N):
    score.append(int(case[i]))
score.sort()
print(sum(score[L:N-H])/(N-L-H))