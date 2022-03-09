import sys
case1 = sys.stdin.readline().strip().split()
N, S = int(case1[0]), int(case1[1])
case2 = sys.stdin.readline().strip().split()
num_list = []
result = []
for i in range(N):
    num_list.append(int(case2[i]))
Sum, end = 0, 0
for start in range(N):
    while end < N and Sum < S:
        Sum += num_list[end]
        end += 1
    if Sum >= S:
        result.append(end - start)
    Sum -= num_list[start]
if result:
    print(min(result))
else:
    print(0)