def prime_list(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True]


def 소인수분해(n):
    A = []
    for i in prime_list(int(n ** 0.5)):
        if n % i == 0:
            A.append(i)
            while n % i == 0:
                n //= i
    if n > 1:
        A.append(n)
    return A


while True:
    n = int(input())
    result = n
    if n == 0:
        break
    else:
        for i in 소인수분해(n):
            result = result * (i-1) // i
        print(result)
