n = int(input())
result_list = []
for i in range(2, int(n ** 0.5) + 1):
    if n % i == 0:
        while n % i == 0:
            n = n // i
        result_list.append(i)
        if i != n // i:
            result_list.append(n // i)
if n > 1:
    result_list.append(n)
print(result_list)