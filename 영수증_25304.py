import sys
X = int(sys.stdin.readline().strip())
N = int(input())
Sum = 0
for _ in range(N):
    a, b = map(int, sys.stdin.readline().strip().split())
    Sum += a * b
if X == Sum:
    print('Yes')
else:
    print('No')