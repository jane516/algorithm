import sys


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


case = sys.stdin.readline().strip()
N = int(case)
a = []
for i in range(len(case)):
    if int(case[i]) != 0:
        a.append(int(case[i]))
a.sort()
for i in range(1, len(a)):
    a[0] = a[0] * a[i] // gcd(a[0], a[i])
if N % a[0] == 0:
    print(N)
else:
    check = 0
    count = 1
    while True:
        for i in range(10**count):
            if (10 * N + i) % a[0] == 0:
                print(10 * N + i)
                check = 1
                break
        if check == 1:
            break
        count += 1
        N *= 10



