dic = {}
N = int(input())
for i in range(N):
    str = list(input())
    d = len(str)
    for j in range(d):
        if str[j] in dic:
            dic[str[j]] += 10**(d-j-1)
        else:
            dic[str[j]] = 10**(d-j-1)
my_list = [i for i in dic.values()]
my_list.sort()
result = 0
for i in range(len(my_list)):
    result += my_list[-1-i] * (9 - i)
print(result)