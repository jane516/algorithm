import sys
case = sys.stdin.readline().strip().split()
X = float(case[0])
Y = float(case[1])
D = float(case[2])
T = float(case[3])
d = (X ** 2 + Y ** 2) ** 0.5

if T >= D:
    print(d)
else:
    if d % D == 0:
        print(d // D * T)
    else:
        if d // D != 0:
            result1 = d // D * T + d % D
            result2 = d // D * T + T
            result3 = d // D * T + T + D - d % D
            print(min(result1, result2, result3))
        else:
            result1 = d
            result2 = 2 * T
            result3 = T + D - d
            print(min(result1, result2, result3))