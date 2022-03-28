import sys
N, M = map(int, input().split())
case = sys.stdin.readline().strip().split()
my_list = []
for i in range(M):
    my_list.append(int(case[i]))
result = []
for i in my_list:
    for j in range(1, N + 1):
        if i * j <= N and i * j not in result:
            result.append(i * j)
print(sum(result))