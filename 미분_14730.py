N = int(input())
Sum = 0
for _ in range(N):
    a, b = map(int, input().split())
    Sum += a * b
print(Sum)