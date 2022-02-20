import math
N = input()
Sum = 0
i = 0
dic = {'1': 1, '2': 2, '6': 3, '24': 4, '120': 5, '720': 6}
if N in dic.keys():
    print(dic[N])
else:
    while True:
        if Sum >= len(N) - 1:
            break
        i += 1
        Sum += math.log10(i)
    print(i)