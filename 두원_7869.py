import math
from math import pi


def 두점거리(x1, y1, x2, y2):
    d = ((x1-x2)**2 + (y1-y2)**2)**0.5
    return d


x1, y1, r1, x2, y2, r2 = map(float, input().split())
r1, r2 = max(r1, r2), min(r1, r2)
d = 두점거리(x1, y1, x2, y2)
if d + r2 <= r1:
    result = pi * r2 ** 2
elif d >= r1 + r2:
    result = 0
else:
    if d**2 > r1**2 - r2**2:
        h = (r1 ** 2 - ((d ** 2 + r1 ** 2 - r2 ** 2) / (2 * d)) ** 2) ** 0.5
        S = r1**2 * math.asin(h/r1) + r2**2 * math.asin(h/r2) - d * h
        result = S
    else:
        x = (r1**2 - r2**2 - d**2)/(2*d)
        S1 = r2**2 * math.acos(x/r2) - x * (r2**2 - x**2)**0.5
        S2 = r1**2 * math.acos((x+d)/r1) - (x+d) * (r2**2 - x**2)**0.5
        result = pi * r2**2 - S1 + S2
print('%.3f' % result)