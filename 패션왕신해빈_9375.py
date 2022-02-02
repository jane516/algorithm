import sys
T = int(input())
for i in range(T):
    n = int(input())
    옷장 = dict()
    result = 1
    for j in range(n):
        case = sys.stdin.readline().strip()
        의상이름 = case.split()[0]
        의상종류 = case.split()[1]
        if 의상종류 in 옷장.keys():
            옷장[의상종류] += 1
        else:
            옷장[의상종류] = 1
    for k in 옷장.keys():
        result *= (옷장[k] + 1)
    print(result - 1)