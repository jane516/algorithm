N = int(input())
sieve = [1] * (N+1)
m = int(N ** 0.5)
count = 1
sieve[1] = 1
for i in range(2, N + 1):
    if sieve[i] == 1:
        count += 1
        for j in range(i, N+1, i):
            sieve[j] = count
print(count)
for i in sieve[1:]:
    print(i, end=' ')