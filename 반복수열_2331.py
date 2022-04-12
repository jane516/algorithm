A, P = map(int, input().split())
D = [A]
n = 1
while True:
    X = D[n-1]
    Sum = 0
    while X > 0:
        Sum += (X % 10) ** P
        X //= 10
    if Sum in D:
        print(D.index(Sum))
        break
    D.append(Sum)
    n += 1
