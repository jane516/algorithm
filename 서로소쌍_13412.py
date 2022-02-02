def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


T = int(input())
for i in range(T):
    count = 0
    N = int(input())
    m = int(N ** 0.5)
    for j in range(1, m + 1):
        if N % j == 0 and gcd(j, N // j) == 1:
            count += 1
    print(count)