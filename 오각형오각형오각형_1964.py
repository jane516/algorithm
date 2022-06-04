import sys
N = int(sys.stdin.readline().strip())
result = (5 + (3 * (N - 1) ** 2 + 11 * (N - 1)) // 2) % 45678
print(result)