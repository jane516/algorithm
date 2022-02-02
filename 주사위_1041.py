N = int(input())
a = list(map(int, input().split()))
Sum = 0
if N == 1:
    for i in range(5):
        a.sort()
        Sum += a[i]
    print(Sum)
else:
    b = [min(a[0], a[5]), min(a[1], a[4]), min(a[2], a[3])]
    b.sort()
    Sum += b[0] * (5 * N ** 2 - 8 * N + 4) + b[1] * (8 * N - 8) + b[2] * 4
    print(Sum)