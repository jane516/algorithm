import sys
N = int(input())
game_list = [0 for _ in range(N)]
for i in range(N):
    case = sys.stdin.readline().strip().split()
    A = []
    for j in range(3):
        for k in range(j + 1, 4):
            for t in range(k + 1, 5):
                A.append((int(case[j]) + int(case[k]) + int(case[t])) % 10)
    game_list[i] = max(A)
result = []
for i in range(N):
    if game_list[i] == max(game_list):
        result.append(i+1)
print(max(result))
