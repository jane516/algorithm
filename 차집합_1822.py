import sys
na, nb = map(int, sys.stdin.readline().strip().split())
A = set(map(int, sys.stdin.readline().strip().split()))
B = set(map(int, sys.stdin.readline().strip().split()))
C = list(A - B)
C.sort()
X = len(C)
if X == 0:
    print(0)
    exit(0)
else:
    print(X)
    print(*C)
