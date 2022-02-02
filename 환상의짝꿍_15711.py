import sys


def prime_list(n):
    sieve = [True] * (n+1)
    for i in range(2, n + 1):
        if sieve[i] == True:
            for j in range(i + i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True]


sieve1 = prime_list(2000000)


def is_prime(n):
    if n > 2000000:
        for i in sieve1:
            if n % i == 0:
                return False
        return True
    else:
        if n == 1:
            return False
        else:
            if n in sieve1:
                return True
            else:
                return False


T = int(input())
for i in range(T):
    case = sys.stdin.readline().strip().split()
    A = int(case[0])
    B = int(case[1])
    if (A + B) % 2 == 0:
        if A + B > 2:
            print('YES')
        else:
            print('NO')
    else:
        if is_prime(A + B - 2):
            print('YES')
        else:
            print('NO')
