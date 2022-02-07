import sys

case = sys.stdin.readline().strip().split()
x, y, c = float(case[0]), float(case[1]), float(case[2])


def 교점높이(x, y, k):
    y_1 = (y**2 - k**2)**0.5
    x_1 = (x**2 - k**2)**0.5
    h = x_1 * y_1 / (x_1 + y_1)
    return h

l = 0
r = min(x, y)
while True:
    mid = (l + r) / 2
    if abs(교점높이(x, y, mid) - c) < 10**(-3):
        print(mid)
        break

    else:
        if 교점높이(x, y, mid) > c + 10**(-3):
            l = mid
        elif 교점높이(x, y, mid) < c - 10**(-3):
            r = mid

