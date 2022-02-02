n = int(input())
A = [1, 3]
count = 0
if n in A:
    print(-1)
else:
    if n % 5 == 1:
        count += (n - 6) // 5
        print(count + 3)
    elif n % 5 == 3:
        count += (n - 8) // 5
        print(count + 4)
    else:
        count += (n % 5) // 2 + n // 5
        print(count)