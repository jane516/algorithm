def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


A, B = map(int, input().split())
C, D = map(int, input().split())
분자 = A * D + B * C
분모 = B * D
GCD = gcd(분자, 분모)
print(분자 // GCD, 분모 // GCD)
