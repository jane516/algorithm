count = 0
while True:
    L, P, V = map(int, input().split())
    count += 1
    if L == 0:
        break
    result = (V // P) * L
    if V % P > L:
        result += L
    else:
        result += V % P
    print("Case {}: {}".format(count, result))
