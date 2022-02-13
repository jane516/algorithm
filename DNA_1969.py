N, M = map(int, input().split())
my_list = []
for i in range(N):
    my_list.append(input())

Sum = 0
for j in range(M):
    B = [[0, 'A'], [0, 'T'], [0, 'G'], [0, 'C']]
    for i in range(N):
        if my_list[i][j] == 'A':
            B[0][0] += 1
        elif my_list[i][j] == 'T':
            B[1][0] += 1
        elif my_list[i][j] == 'G':
            B[2][0] += 1
        else:
            B[3][0] += 1
    Sum += N - max(B)[0]
    result = []
    for i in range(4):
        if B[i][0] == max(B)[0]:
            result.append(B[i][1])
    result.sort()
    print(result[0], end='')
    if j == M - 1:
        print(' ')
print(Sum)

