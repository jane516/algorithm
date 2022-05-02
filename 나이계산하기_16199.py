Y, M, D = map(int, input().split())
NY, NM, ND = map(int, input().split())
result = [0, 0, 0]
result[1] = NY - Y + 1
result[2] = NY - Y
if NY == Y:
    result[0] = 0
else:
    if NM < M:
        result[0] = NY - Y - 1
    elif NM == M and ND < D:
        result[0] = NY - Y - 1
    else:
        result[0] = NY - Y
for i in range(3):
    print(result[i])