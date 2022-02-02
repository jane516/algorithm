from itertools import combinations
L, C = map(int, input().split())
A = list(input().split())
A.sort()
B = list(combinations(A, L))
Sum = 0
for i in range(len(B)):
    Sum += B[i].count('a')
    Sum += B[i].count('e')
    Sum += B[i].count('i')
    Sum += B[i].count('o')
    Sum += B[i].count('u')
    if Sum >= 1:
        if Sum < L-1:
            print(''.join(B[i]))
    Sum = 0


