import sys
N = int(sys.stdin.readline().strip())
num_list = [i for i in range(1, N + 1)]
sum_list = [0 for _ in range(N)]
sum_list[0] = 1
count = 0

for i in range(1, N):
    sum_list[i] += num_list[i] + sum_list[i - 1]

for i in range(N - 1):
    for j in range(i + 1, N):
        if sum_list[j] > sum_list[i] + N:
            break
        elif sum_list[j] == sum_list[i] + N:
            count += 1
count += sum_list.count(N)
print(count)
