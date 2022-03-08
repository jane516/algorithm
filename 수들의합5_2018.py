import sys
N = int(sys.stdin.readline().strip())
sum_list = [i * (i + 1) // 2 for i in range(1, N // 2 + 2)]

count = 0

for i in range(N // 2):
    for j in range(i, N // 2 + 1):
        if sum_list[j] > sum_list[i] + N:
            break
        elif sum_list[j] == sum_list[i] + N:
            count += 1
count += sum_list.count(N)
if N == 1:
    print(1)
elif N == 2:
    print(1)
else:
    print(count + 1)
