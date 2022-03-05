N = int(input())
dic = {}
my_list = []
for i in range(N):
    number = input()
    my_list.append(number[0])
    for j in range(len(number)):
        if number[j] in dic:
            dic[number[j]] += 10**(len(number)-j-1)
        else:
            dic[number[j]] = 10**(len(number)-j-1)

dic.items()
dic = sorted(dic.items(), key=lambda x: x[1], reverse=True)
Sum = 0
if len(dic) == 10 and dic[-1][0] in my_list:
    k = 1
    for i in range(len(dic)):
        X = dic.pop()
        if X[0] not in my_list:
            break
        else:
            Sum += X[1] * k
            k += 1
    for i in range(len(dic)):
        X = dic.pop()
        Sum += X[1] * k
        k += 1
else:
    k = 9
    for i in dic:
        Sum += i[1] * k
        k -= 1

print(Sum)