import sys
N = int(sys.stdin.readline().strip())
A = list(map(int, sys.stdin.readline().strip().split()))
Sum = [0 for _ in range(N + 1)]
result = 0
for i in range(1, N+1):
    Sum[i] = A[i-1] + Sum[i-1]
for i in range(N):
    result += A[i] * (Sum[-1] - Sum[i+1]) % 1000000007
print(result % 1000000007)