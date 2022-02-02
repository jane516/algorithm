def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


N = int(input())
factor = list(map(int, input().split()))
전체곱 = 1
부분곱의합 = 0
for i in range(N):
    전체곱 *= factor[i]
for j in range(N):
    부분곱의합 += 전체곱 // factor[j]
GCD = gcd(전체곱, 부분곱의합)
print(전체곱 // GCD, end='')
print('/', end='')
print(부분곱의합 // GCD)