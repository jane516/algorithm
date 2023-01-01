import sys
import math

b, c, a1, a2 = map(int, sys.stdin.readline().strip().split())

result = (b + math.sqrt(b ** 2 + 4 * c)) / 2

print(result)