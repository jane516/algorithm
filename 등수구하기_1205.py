import sys
N, new_score, P = map(int, sys.stdin.readline().strip().split())
score_list = [0 for _ in range(N)]
result = 0
if N == 0:
    result = 1
else:
    score_list = list(map(int, sys.stdin.readline().strip().split()))
    if N == P and score_list[-1] >= new_score:
        result = -1
    else:
        result = N + 1
        for i in range(N):
            if score_list[i] <= new_score:
                result = i + 1
                break
print(result)