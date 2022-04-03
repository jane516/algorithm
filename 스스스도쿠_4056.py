T = int(input())
for i in range(T):
    a = [[0 for _ in range(9)] for _ in range(9)]
    Count = 0
    for j in range(9):
        number_list = list(input())
        for k in range(9):
            a[j][k] = int(number_list[k])
    for j in range(9):
        if a[j].count(0) == 1:
            idx = a[j].index(0)
            a[j][idx] = 45 - sum(a[j])
            if a[j][idx] <= 0:
                print('Could not complete this grid.')
                if i < T - 1:
                    print()
                exit(0)
            Count += 1
    if Count == 5:
        for j in range(9):
            if sum(a[j]) != 45:
                print('Could not complete this grid.')
                if i < T - 1:
                    print()
                exit(0)
        for j in range(9):
            for k in range(9):
                if k == 8:
                    print(a[j][k])
                    break
                print(a[j][k], end='')
        if i < T - 1:
            print()
    else:
        for j in range(9):
            Sum = 0
            check = 0
            idx = 0
            for k in range(9):
                Sum += a[k][j]
                if a[k][j] == 0:
                    idx = k
                    check += 1
            if check == 1:
                a[idx][j] = 45 - Sum
                if a[idx][j] <= 0:
                    print('Could not complete this grid.')
                    if i < T - 1:
                        print()
                    exit(0)
                Count += 1
        if Count == 5:
            for j in range(9):
                if sum(a[j]) != 45:
                    print('Could not complete this grid.')
                    if i < T - 1:
                        print()
                    exit(0)
            for j in range(9):
                for k in range(9):
                    if k == 8:
                        print(a[j][k])
                        break
                    print(a[j][k], end='')
            if i < T - 1:
                print()
        else:
            for l in range(3):
                for j in range(3):
                    check = 0
                    Sum = 0
                    idx1, idx2 = 0, 0
                    for k in range(3):
                        for t in range(3):
                            Sum += a[3*l+k][3*j+t]
                            if a[3*l+k][3*j+t] == 0:
                                check += 1
                                idx1, idx2 = k, t
                    if check == 1:
                        a[3 * l + idx1][3 * j + idx2] = 45 - Sum
                        if a[3 * l + idx1][3 * j + idx2] <= 0:
                            print('Could not complete this grid.')
                            if i < T - 1:
                                print()
                            exit(0)
                        Count += 1
            if Count == 5:
                for j in range(9):
                    if sum(a[j]) != 45:
                        print('Could not complete this grid.')
                        if i < T - 1:
                            print()
                        exit(0)
                for j in range(9):
                    for k in range(9):
                        if k == 8:
                            print(a[j][k])
                            break
                        print(a[j][k], end='')
                if i < T - 1:
                    print()
            else:
                print('Could not complete this grid.')
                if i < T - 1:
                    print()
