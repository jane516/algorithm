import sys
num = list(map(int, sys.stdin.readline().strip().split()))
num.sort()
a, b, c = num[0], num[1], num[2]
if b - a == c - b:
    print(2 * a - b)
elif b - a < c - b:
    print((b + c) // 2)
else:
    print((a + b) // 2)