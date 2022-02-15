import sys
case1 = sys.stdin.readline().strip().split()
N, K = int(case1[0]), int(case1[1])
case2 = sys.stdin.readline().strip().split()
card_list = []
for i in range(K):
    card_list.append(int(case2[i]))
card_list.sort()
result = [1 for _ in range(N + 1)]
for i in range(N + 1):
    for j in card_list:
        if result[j] == 1:
            for k in range(j, N + 1, j):
                result[k] = 0
print(N - result[1:].count(1))