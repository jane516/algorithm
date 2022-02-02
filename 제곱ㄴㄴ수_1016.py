import sys
case = sys.stdin.readline().strip()
min = int(case.split()[0])
max = int(case.split()[1])
sieve = [1] * (max - min + 1)
i = 2
while i * i <= max:
    if (min // i**2) * (i**2) < min:
        A = ((min // i**2)+1) * (i**2)
    else:
        A = (min // (i**2)) * (i**2)
    for j in range(A, max+1, i**2):
        sieve[j - min] = 0
    i += 1
print(sieve.count(1))

