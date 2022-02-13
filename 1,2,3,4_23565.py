import sys
T = int(input())
for i in range(T):
    case = sys.stdin.readline().strip().split()
    a, b, c, d = int(case[0]), int(case[1]), int(case[2]), int(case[3])
    if a == 0 and b == 0:
        if c >= 4 and d >= 3:
            result = (c + 1) * (d + 1)
            result -= (c - 3) * (d - 2)
            result += min(c // 4, d // 3)
            print(result)
        else:
            result = (c + 1) * (d + 1)
            print(result)
    elif a == 0:
        b += d * 2
        if b >= 3 and c >= 2:
            result = (c + 1) * (d + 1)
            result -= (b - 2) * (c - 1)
            result += min(b // 3, c // 2)
            print(result)
        else:
            result = (b + 1) * (c + 1)
            print(result)
    elif b == 0:
        if a == 3:
            a += c * 3
            result = (a + 1) * (d + 1)
            print(result)
        elif a > 3:
            a += c * 3 + d * 4
            result = a + 1
            print(result)
        else:
            if d == 0:
                print((a + 1) * (c + 1))
            elif c == 0:
                print((a + 1) * (d + 1))
            else:
                if a == 2:
                    print(2 + c * 3 + d * 4 + 1)
                else:
                    if c == 1:
                        print(1 + 3 + d * 4 + 1 - 3)
                    else:
                        print(1 + 3 * c + 4 * d + 1 - 2)

    else:
        b += 2 * d + c
        a += 2 * b + c
        print(a + 1)