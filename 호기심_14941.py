import sys
N = int(input())

def prime_list(n):
    sieve = [1] * (n+1)
    for i in range(2, n + 1):
        if sieve[i] == 1:
            for j in range(i + i, n+1, i):
                sieve[j] = 0
    return [i for i in range(2, n+1) if sieve[i] == 1]


Prime = prime_list(100000)


for j in range(N):
    case = sys.stdin.readline().strip().split()
    a = int(case[0])
    b = int(case[1])
    A = []
    for i in range(a, b + 1):
        if i in Prime:
            A.append(i)
