def fac_non_zero(n):
    result = 1
    count = 0
    for i in range(1, n + 1):
        result *= i
    while result % 10 == 0:
        result //= 10
    return result % 10


t = int(input())
for i in range(t):
    n = int(input())
    print(fac_non_zero(n))