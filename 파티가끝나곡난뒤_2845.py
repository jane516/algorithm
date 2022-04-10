import sys
L, P = map(int, input().split())
case = sys.stdin.readline().strip().split()
result = [0 for _ in range(5)]
for i in range(5):
    result[i] = int(case[i]) - L * P
print(*result)