def 오의개수(N):
    count = 0
    while N // 5 > 0:
        count += N // 5
        N //= 5
    return count


N = int(input())
result = 1
for i in range(N):
    result *= (i + 1)
    while result % 10 == 0:
        result //= 10
    result %= 100000000
print(result % 10)