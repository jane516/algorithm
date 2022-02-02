N = int(input())
T = N
Count = 0
while T > 0:
    T //= 10
    Count += 1
result = Count*N - Count*((10**(Count-1))-1) + (Count-1) * (10**(Count-1)) - (10**(Count-1)-1)//9
print(result)