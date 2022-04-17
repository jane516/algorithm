import sys
case = sys.stdin.readline().strip().split()
N, M = int(case[0]), int(case[1])
my_list = [0 for _ in range(N)]
for i in range(N):
    my_list[i] = int(sys.stdin.readline().strip())
my_list.sort()
result = []
end = 0
for start in range(N):
    while end < N:
        if end == N - 1:
            break
        if my_list[end] - my_list[start] >= M:
            break
        end += 1
    if my_list[end] - my_list[start] >= M:
        result.append(my_list[end] - my_list[start])
print(min(result))