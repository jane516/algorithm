import sys


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
            while n % i == 0:
                A.append(i)
                n //= i
    if n > 1:
        A.append(n)
    return A


N = int(input())
case1 = sys.stdin.readline().strip().split()
N_list = []
for i in range(N):
    for j in 소인수분해(int(case1[i])):
        N_list.append(j)
M = int(input())
case2 = sys.stdin.readline().strip().split()
M_list = []
for i in range(M):
    for j in 소인수분해(int(case2[i])):
        M_list.append(j)

result = 1
for i in set(N_list) & set(M_list):
    result *= i ** min(N_list.count(i), M_list.count(i)) % 10**10
if len(str(result)) < 10:
    print(result)
else:
    print(str(result % 10**10)[1:])

