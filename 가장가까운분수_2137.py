def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


a, b = map(int, input().split())
MIN = 1
MIN_a = 0
MIN_b = 0
for i in range(32767, 0, -1):
    for j in range(1, i):
        if gcd(i, j) == 1 and b * j != a * i:
            if abs(a/b - j/i) < MIN:
                MIN = abs(a/b - j/i)
                MIN_a = j
                MIN_b = i
print(MIN_a, MIN_b)
