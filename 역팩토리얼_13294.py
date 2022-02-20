import sys
import math
N = int(sys.stdin.readline().strip())
Sum = 0
i = 1
while True:
    if Sum >= int(math.log10(N)):
        break
    Sum += math.log10(i)
    i += 1
print(i - 1)
print(len(str(N)))