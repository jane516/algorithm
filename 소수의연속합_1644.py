import sys
N = int(sys.stdin.readline().strip())


def prime_list(n):
    sieve = [True] * (n+1)
    m = int(n ** 0.5)
    for i in range(2, m + 1):
        if sieve[i] == True:
            for j in range(i + i, n+1, i):
                sieve[j] = False
    return [i for i in range(2, n+1) if sieve[i] == True]


my_list = prime_list(N)
start, end = 0, 0
Sum = 0
count = 0
for start in range(len(my_list)):
    while Sum < N and end < len(my_list):
        Sum += my_list[end]
        end += 1
    if Sum == N:
        count += 1
    Sum -= my_list[start]
print(count)