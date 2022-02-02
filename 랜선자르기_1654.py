import sys
case = sys.stdin.readline().strip().split()
K = int(case[0])
N = int(case[1])
A = []
for i in range(K):
    A.append(int(input()))
A.sort()
l = 1
r = A[-1]
while l <= r:
    count = 0
    mid = (l + r) // 2
    for i in range(K):
        count += A[i] // mid
    if count < N:
        r = mid - 1
    elif count >= N:
        l = mid + 1
print(r)
