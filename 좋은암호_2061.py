import sys
K, L = map(int, sys.stdin.readline().strip().split())
check = 0


def prime_list(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True]


my_list = prime_list(L - 1)

for i in my_list:
    a = K % i
    if a == 0:
        print('BAD', i)
        check = 1
        break

if check == 0:
    print('GOOD')