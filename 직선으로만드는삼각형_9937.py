import sys


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


N = int(input())
ABC_list = [[0 for _ in range(3)] for _ in range(N)]
tan_list = []
Sum = 0
for i in range(N):
    case = sys.stdin.readline().strip().split()
    ABC_list[i][0], ABC_list[i][1], ABC_list[i][2] = int(case[0]), int(case[1]), int(case[2])
    if ABC_list[i][0] == 0:
        tan_list.append('y')
    elif ABC_list[i][1] == 0:
        tan_list.append('x')
    else:
        GCD = gcd(ABC_list[i][0], ABC_list[i][1])
        if ABC_list[i][0] < 0:
            ABC_list[i][0], ABC_list[i][1] = - ABC_list[i][0], - ABC_list[i][1]
        ABC_list[i][0], ABC_list[i][1] = ABC_list[i][0] // GCD, ABC_list[i][1] // GCD




    if ABC_list[i][1] == 0:
        tan_list.append('x')
    else:
        tan_list.append(ABC_list[i][0] / ABC_list[i][1])
my_list = list(set(tan_list))
dic = {my_list[i]: tan_list.count(my_list[i]) for i in range(len(my_list))}
for i in dic.values():
    if i >= 2:
        Sum += ((N - i) * (i * (i - 1) // 2) + i * (i - 1) * (i - 2) // 6) % 1000000007
result = (N * (N - 1) * (N - 2) // 6 - Sum) % 1000000007
print(result)