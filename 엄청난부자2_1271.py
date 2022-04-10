import sys
case = sys.stdin.readline().strip().split()
n, m = int(case[0]), int(case[1])
print(n // m)
print(n % m)