P = int(input())
Q = int(input())
goal = [0, 1, 4, 6, 8, 9, 10, 12, 14, 15, 16, 18]
p = P / 100
q = Q / 100


def Combination(n, r):
    if n-r < r:
        r = n - r
    분자 = 분모 = 1
    for i in range(r):
        분자 *= (n-i)
        분모 *= (i+1)
    return 분자 // 분모


A = B = 0
for i in goal:
    A += Combination(18, i) * p ** i * (1 - p)**(18-i)
    B += Combination(18, i) * q ** i * (1 - q)**(18-i)
print(1 - A * B)