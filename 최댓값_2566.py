import sys
Max = 0
x, y = 0, 0
for j in range(9):
    a = list(map(int, sys.stdin.readline().strip().split()))
    M = max(a)
    Max = max(Max, max(a))
    if Max == M:
        x, y = j + 1, a.index(M) + 1
print(Max)
print(x, y)