a, b, c = map(int, input().split())
if a == b and b == c:
    print(10000 + a * 1000)
elif a != b and b != c and c != a:
    Max = max(a, b)
    Max = max(Max, c)
    print(Max * 100)
else:
    if a == b:
        print(1000 + a * 100)
    elif b == c:
        print(1000 + b * 100)
    else:
        print(1000 + a * 100)