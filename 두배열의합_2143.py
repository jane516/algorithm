import sys
import bisect
T = int(sys.stdin.readline().strip())
n = int(input())
A = list(map(int, sys.stdin.readline().strip().split()))
m = int(input())
B = list(map(int, sys.stdin.readline().strip().split()))
Asum = []
for i in range(n):
    sum = 0
    for j in range(i, n):
        sum += A[j]
        Asum.append(sum)
Bsum = []
for i in range(m):
    sum = 0
    for j in range(i, m):
        sum += B[j]
        Bsum.append(sum)
count = 0
Bsum.sort()
for i in Asum:
    k = T - i
    left = bisect.bisect_left(Bsum, k)
    right = bisect.bisect_right(Bsum, k)
    count += right - left
print(count)