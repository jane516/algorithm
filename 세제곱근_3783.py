import sys
T = int(input())
for i in range(T):
    a = int(sys.stdin.readline().strip())
    l, r = 0, a
    x = a
    while True:
        if abs(x**3 - a) < 0.00000000001:
            break
        m = (l + r) / 2
        if x ** 3 < a:
            l = m
        else:
            r = m
    print(x)