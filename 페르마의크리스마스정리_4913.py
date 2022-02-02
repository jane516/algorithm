n = 1000001
sieve = [1] * n
m = int(n ** 0.5)
B = [0] * n
C = [0] * n
for i in range(2, n):
    B[i] = B[i-1]
    C[i] = C[i-1]
    if sieve[i] == 1:
        B[i] += 1
        if i % 4 == 1 or i == 2:
            C[i] += 1
        for j in range(i + i, n, i):
            sieve[j] = 0

while True:
    L, U = map(int, input().split())
    T = L
    if L == -1 and U == -1:
        break
    if U < 2:
        print(L, U, 0, 0)
    else:
        if L < 1:
            T = 1
        print(L, U, B[U] - B[T-1], C[U] - C[T-1])

