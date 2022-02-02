def 체스판칠하기(x, y):
    good1 = bad1 = 0
    good2 = bad2 = 0
    for i in range(x, x+8):
        for j in range(y, y+8):
            if i % 2 == 0 and j % 2 == 0:
                if A[i][j] == 'W':
                    good1 += 1
                else:
                    bad1 += 1
            elif i % 2 == 0 and j % 2 == 1:
                if A[i][j] == 'B':
                    good1 += 1
                else:
                    bad1 += 1
            elif i % 2 == 1 and j % 2 == 0:
                if A[i][j] == 'B':
                    good1 += 1
                else:
                    bad1 += 1
            elif i % 2 == 1 and j % 2 == 1:
                if A[i][j] == 'W':
                    good1 += 1
                else:
                    bad1 += 1
            if i % 2 == 0 and j % 2 == 0:
                if A[i][j] == 'B':
                    good2 += 1
                else:
                    bad2 += 1
            elif i % 2 == 0 and j % 2 == 1:
                if A[i][j] == 'W':
                    good2 += 1
                else:
                    bad2 += 1
            elif i % 2 == 1 and j % 2 == 0:
                if A[i][j] == 'W':
                    good2 += 1
                else:
                    bad2 += 1
            elif i % 2 == 1 and j % 2 == 1:
                if A[i][j] == 'B':
                    good2 += 1
                else:
                    bad2 += 1
    if good1 > good2:
        return bad1
    else:
        return bad2


N, M = map(int, input().split())
A = [[] * M] * N
for k in range(N):
    A[k] = list(input())
Count = []
for i in range(N - 7):
    for j in range(M - 7):
        Count.append(체스판칠하기(i, j))
print(min(Count))
