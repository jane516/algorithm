def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


A, B = map(int, input().split())
pq = B // A
if pq == 1:
    print(A, A)
else:
    for i in range(int(pq ** 0.5) + 1, pq + 1):
        if pq % i == 0 and gcd(i, pq // i) == 1:
            print((pq * A) // i, i * A)
            break