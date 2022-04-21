import sys
case = sys.stdin.readline().strip().split()
N, K = int(case[0]), int(case[1])
A = list(map(int, sys.stdin.readline().strip().split()))
my_list = [0 for _ in range(N + 1)]
for i in range(1, N + 1):
    my_list[i] = my_list[i-1] + A[i-1]
cnt = 0
for start in range(N):
    end = start + 1
    while end < N + 1:
        if my_list[end] - my_list[start] == K:
            cnt += 1
        end += 1
print(cnt)