def 자리수합(n):
    a, b, c = n, n, n
    result1, result2, result3 = 0, 0, 0
    while a > 0:
        result1 += a % 10
        a //= 10
    while b > 0:
        result2 += b % 12
        b //= 12
    while c > 0:
        result3 += c % 16
        c //= 16
    if result1 == result2 == result3:
        print(n)


for i in range(2992, 10000):
    자리수합(i)