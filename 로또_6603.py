import itertools

while True:
    a = list(map(int, input().split()))
    if a[0] == 0:
        break
    로또_list = a[1:]
    result = list(itertools.combinations(로또_list, 6))
    for i in range(len(result)):
        for j in range(len(list(result[i]))):
            print(list(result[i])[j], end=' ')
        print()
    print()