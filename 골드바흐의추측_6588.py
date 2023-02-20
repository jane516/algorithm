import sys

n = 1000001
Prime = [True] * n
m = int(n ** 0.5)
for i in range(2, m + 1):
    if Prime[i] == True:
        for j in range(i + i, n, i):
            Prime[j] = False


while True:
    n = int(sys.stdin.readline().strip())
    Check = 0
    if n == 0:
        break
    for i in range(3, n // 2 + 1):
        if Prime[i] == False:
            continue
        if Prime[n-i] == True:
            print("%d = %d + %d"%(n, i, n-i))
            Check = 1
            break
    if Check == 0:
        print("Goldbach's conjecture is wrong.")