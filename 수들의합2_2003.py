import sys
case1 = sys.stdin.readline().strip().split()
N, M = int(case1[0]), int(case1[1])
case2 = sys.stdin.readline().strip().split()
num_list = []
sum_list = [0 for _ in range(N)]
for i in range(N):
    num_list.append(int(case2[i]))
sum_list[0] = num_list[0]
for i in range(1, N):
    sum_list[i] += num_list[i] + sum_list[i-1]
count = 0
for i in range(N - 1):
    for j in range(i + 1, N):
        if sum_list[j] > sum_list[i] + M:
            break
        elif sum_list[j] == sum_list[i] + M:
            count += 1
count += sum_list.count(M)
print(count)