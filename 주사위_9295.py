import sys
N = int(sys.stdin.readline().strip())
while N % 2 == 0:
    N //= 2
if N == 1:
    print(1)
else:
    print(0)