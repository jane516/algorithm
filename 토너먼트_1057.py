N, A, B = map(int, input().split())
A, B = min(A, B), max(A, B)
count = 0
while True:
    if A == B:
        break
    if A % 2 != 0:
        A += 1
    if B % 2 != 0:
        B += 1
    A //= 2
    B //= 2
    count += 1
print(count)