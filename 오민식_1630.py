import sys


def prime_list(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True]


N = int(sys.stdin.readline().strip())
my_list = prime_list(N)
result = 1

for i in my_list:
    A = N
    while A >= i:
        result *= i % 987654321
        A //= i

print(result % 987654321)