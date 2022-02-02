import sys

N = int(sys.stdin.readline())
A = [0] * 10001
for i in range(N):
    n = int(sys.stdin.readline())
    A[n] += 1
for j in range(1, 10001):
    count = A[j]
    for k in range(count):
        print(j)
