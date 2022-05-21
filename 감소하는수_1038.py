import sys
from itertools import combinations
N = int(sys.stdin.readline().strip())
result = []
for i in range(1, 11):
    for j in combinations(range(0, 10), i):
        num = list(j)
        num.sort(reverse=True)
        result.append(int("".join(map(str, num))))
result.sort()
if N >= len(result):
    print(-1)
else:
    print(result[N])