N = list(map(int, input()))
number = [0] * 9
for j in N:
    if j == 6 or j == 9:
        number[6] += 1
    else:
        number[j] += 1

if number[6] % 2 == 0:
    number[6] //= 2
else:
    number[6] = (number[6] + 1) // 2
print(max(number))