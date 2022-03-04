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
k = 9
print(dic)
print(dic[0:len(dic)-2])
for i in dic[0:len(dic)-2]:
    Sum += k * i[1]
    k -= 1
if dic[-1][0] in my_list:
    Sum += dic[-1][1]
else:
    Sum += dic[-2][1]
print(my_list)
print(Sum)