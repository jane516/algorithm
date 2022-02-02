import sys
case = sys.stdin.readline().strip().split()
a = int(case[0])
d = int(case[1])
k = int(case[2])
if (k - a) % d == 0 and (k - a) // d >= 0:
    print((k - a) // d + 1)
else:
    print("X")