number_list = [0] * 46
for i in range(1, 46):
    number_list[i] = i * (i + 1) // 2
A, B = map(int, input().split())
Sum = 0
check1 = check2 = 0
for i in range(46):
    if A <= number_list[i]:
        check1 = i
        break
for i in range(46):
    if B <= number_list[i]:
        check2 = i
        break
if check1 == check2:
    Sum += check1 * (B - A + 1)
elif check1 + 1 == check2:
    Sum += (check1 * (check1 + 1) // 2 - A + 1) * check1
    Sum += (B - (check2 ** 2 - check2 + 2) // 2 + 1) * check2
else:
    Sum += (check1 * (check1 + 1) // 2 - A + 1) * check1
    Sum += (B - (check2 ** 2 - check2 + 2) // 2 + 1) * check2
    for i in range(check1 + 1, check2):
        Sum += i ** 2
print(Sum)