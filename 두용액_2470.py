import sys

N = int(sys.stdin.readline().strip())
L = list(map(int, sys.stdin.readline().strip().split()))
drink = []

for i in L:
    if i < 0:
        drink.append((abs(i), 0))
    else:
        drink.append((i, 1))

drink.sort()
Sum = 2000000000
a, b = 0, 0

for i in range(1, N):
    if drink[i][1] == drink[i - 1][1]:
        Sum = min(Sum, drink[i][0] + drink[i - 1][0])
        continue
    if abs(drink[i][0] - drink[i - 1][0]) < Sum:
        Sum = abs(drink[i][0] - drink[i - 1][0])
        if drink[i][1] == 0:
            a, b = - drink[i][0], drink[i - 1][0]
        else:
            a, b = - drink[i - 1][0], drink[i][0]

if a == 0:
    if drink[0][1] == 0:
        print(- drink[1][0], - drink[0][0])
    else:
        print(drink[0][0], drink[1][0])
else:
    print(a, b)