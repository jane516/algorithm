import sys
T = int(input())
for i in range(T):
    case = sys.stdin.readline().strip().split()
    P = int(case[0])
    M = int(case[1])
    F = int(case[2])
    C = int(case[3])
    coupon2 = (M // P) * C
    if coupon2 > C:
        print((coupon2 - C) // (F - C) - coupon2 // F)
    else:
        print(0)
