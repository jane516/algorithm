import itertools
X = list(input())
Y = list(map(''.join, itertools.permutations(X)))
Y.sort()
check = 0
for i in Y:
    if int(i) > int(''.join(X)):
        print(i)
        check = 1
        break
if check == 0:
    print(0)