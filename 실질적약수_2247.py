import sys
n = int(sys.stdin.readline().strip())
Sum = 0
for i in range(2, n // 2 + 1):
    Sum += i * (n // i - 1) % 1000000
print(Sum % 1000000)