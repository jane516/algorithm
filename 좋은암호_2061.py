import sys
K, L = map(int, sys.stdin.readline().strip().split())


def prime_list(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True]


my_list = prime_list(K)

for i in range(2, int(K ** 0.5) + 1):
    a = K % i
    if a == 0 and i >= L:
        print('GOOD')
        break
    elif a == 0 and i < L:
        print('BAD', i)
        break