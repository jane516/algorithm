import sys
import string
N = int(sys.stdin.readline().strip())
dic = {}
for _ in range(N):
    Str = sys.stdin.readline().strip()
    for i in range(len(Str)):
        point = Str[i]
        if point in dic:
            dic[point] += 36 ** (len(Str) - 1 - i)
        else:
            dic[point] = 36 ** (len(Str) - 1 - i)
my_list = []
K = int(sys.stdin.readline().strip())
l = len(dic)
for i in dic:
    x = dic[i]
    my_list.append([35 * x - int(i, 36) * x, 35 * x, i])
my_list.sort()
Sum = 0
if K >= l:
    for i in dic:
        Sum += 35 * dic[i]
else:
    for i in range(l - K):
        Sum += int(my_list[i][2], 36) * dic[my_list[i][2]]
    for i in range(K):
        Sum += my_list[-1-i][1]

tmp = string.digits+string.ascii_uppercase


def convert(num, base):
    q, r = divmod(num, base)
    if q == 0:
        return tmp[r]
    else:
        return convert(q, base) + tmp[r]


result = convert(Sum, 36)
print(result)