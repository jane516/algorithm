def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


N = int(input())
for i in range(N):
    b = []
    a = list(map(int, input().split()))
    for j in range(len(a)):
        for k in range(j+1, len(a)):
            b.append(gcd(a[j], a[k]))
    b.sort()
    print(b[-1])
