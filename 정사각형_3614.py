def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


N = int(input())
count = 0
for k in range(1, N + 1):
    if N % k == 0:
        for i in range(1, (1 + N // k) // 2 + 1):
            if gcd(i, 1+N//k-i) == 1:
                count += 1
print(count)