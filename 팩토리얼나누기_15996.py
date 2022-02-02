N, A = map(int, input().split())
Sum = 0
T = A
while N // A > 0:
    Sum += N // A
    A *= T
print(Sum)