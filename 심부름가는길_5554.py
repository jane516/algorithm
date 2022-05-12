import sys
Sum = 0
for _ in range(4):
    Sum += int(sys.stdin.readline().strip())
print(Sum // 60)
print(Sum % 60)