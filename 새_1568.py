import sys
N = int(sys.stdin.readline().strip())
k = 1
count = 0
while N:
    if N < k:
        k = 1
    N -= k
    count += 1
    k += 1
print(count)