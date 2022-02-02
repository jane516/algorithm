N, K = map(int, input().split())
Count = 0
sieve = [True] * N
for i in range(2, N+1):
    if sieve[i-2] == True:
        for j in range(i-2, N-1, i):
            if sieve[j] == True:
                Count += 1
                sieve[j] = False
                if Count == K:
                    print(j+2)