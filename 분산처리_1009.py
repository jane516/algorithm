def power(a, n, mod):
    if n == 1:
        return a
    else:
        t = power(a, n // 2, mod)
        if n % 2 == 0:
            return t * t % mod
        else:
            return t * t * a % mod


T = int(input())
for i in range(T):
    a, b = map(int, input().split())
    result = power(a, b, 10) % 10
    if result == 0:
        print(10)
    else:
        print(result)