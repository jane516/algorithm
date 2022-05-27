import itertools

N = int(input())
my_list = [i for i in range(1, N + 1)]
result = list(itertools.permutations(my_list, N))
for i in range(len(result)):
    for j in range(N - 1):
        print(result[i][j], end=' ')
    print(result[i][N-1])
