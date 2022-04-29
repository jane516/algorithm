import sys
N = int(sys.stdin.readline().strip())
menu = list(map(int, sys.stdin.readline().strip().split()))
menu.sort()
result = 0
for i in range(N):
    result += menu[i] * (pow(2, i, 1000000007) - pow(2, N - i - 1, 1000000007)) % 1000000007
print(result % 1000000007)