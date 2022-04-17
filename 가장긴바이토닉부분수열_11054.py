import sys
N = int(input())
case1 = list(map(int, sys.stdin.readline().strip().split()))
case2 = case1[::-1]
increase = [1 for _ in range(N)]
decrease = [1 for _ in range(N)]
for i in range(N):
    for j in range(i):
        if case1[i] > case1[j]:
            increase[i] = max(increase[i], increase[j] + 1)
        if case2[i] > case2[j]:
            decrease[i] = max(decrease[i], decrease[j] + 1)
result = [0 for _ in range(N)]
for i in range(N):
    result[i] = increase[i] + decrease[N-i-1] - 1
print(max(result))