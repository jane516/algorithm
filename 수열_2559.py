import sys
N, K = map(int, sys.stdin.readline().strip().split())
case = list(map(int, sys.stdin.readline().strip().split()))
my_list = [0 for _ in range(N + 1)]
my_list[0] = 0
for i in range(1, N + 1):
    my_list[i] = my_list[i-1] + case[i - 1]
result = []
for start in range(1, N - K + 2):
    result.append(my_list[start+K-1] - my_list[start-1])
print(max(result))
