def power(a, n, c):
    if n == 1:
        return a % c
    temp = power(a, n // 2, c)
    if n % 2 == 0:
        return temp * temp % c
    else:
        return temp * temp * a % c


A, B, C = map(int, input().split())
print(power(A % C, B, C))