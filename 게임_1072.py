import sys
case = sys.stdin.readline().strip()
X = int(case.split()[0])
Y = int(case.split()[1])
if Y * 100 // X >= 99:
    print(-1)
else:
    left = 1
    right = X
    while left < right:
        mid = (left + right) // 2
        if (Y + mid) * 100 // (X + mid) > Y * 100 // X:
            right = mid
        else:
            left = mid + 1
    print(right)
