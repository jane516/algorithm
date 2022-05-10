N = int(input())
result1 = str(pow(5, N))
l = len(result1)
list = [0 for _ in range(N - l)]
print('0.', end='')
for i in range(len(list)):
    print(list[i], end='')
print(result1)