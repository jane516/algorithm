import sys
N = int(sys.stdin.readline().strip())
Sum = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    Sum += a * b * pow(2, b - 1, 10**9+7) % (10**9+7)
print(Sum % (10**9+7))