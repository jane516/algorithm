import sys

k = int(sys.stdin.readline().strip())
a, b, c, d = map(int, sys.stdin.readline().strip().split())

result1 = a * k + b
result2 = c * k + d

if result1 == result2:
    print('Yes', result1)
else:
    print('No')