import sys


def prime_list(n):
    sieve = [1 for _ in range(n + 1)]
    m = int(n ** 0.5) + 1
    for i in range(2, m):
        if sieve[i] == 1:
            for j in range(i + i, n + 1, i):
                sieve[j] = 0
    return sieve


is_prime = prime_list(1000000)

T = int(input())
for i in range(T):
    Sum = 0
    N = int(sys.stdin.readline().strip())
    for j in range(2, N // 2 + 1):
        if is_prime[j] and is_prime[N - j]:
            Sum += 1
    print(Sum)