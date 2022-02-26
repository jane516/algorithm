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
dic = {'x': 0, 'y': 0}
Sum = 0
for i in range(N):
    case = sys.stdin.readline().strip().split()
    ABC_list[i][0], ABC_list[i][1], ABC_list[i][2] = int(case[0]), int(case[1]), int(case[2])
    if ABC_list[i][0] == 0:
        dic['y'] += 1
    elif ABC_list[i][1] == 0:
        dic['x'] += 1
    else:
        if ABC_list[i][0] < 0:
            ABC_list[i][0], ABC_list[i][1] = - ABC_list[i][0], - ABC_list[i][1]
        GCD = gcd(ABC_list[i][0], ABC_list[i][1])
        ABC_list[i][0], ABC_list[i][1] = ABC_list[i][0] // GCD, ABC_list[i][1] // GCD
        if (ABC_list[i][0], ABC_list[i][1]) in dic:
            dic[(ABC_list[i][0], ABC_list[i][1])] += 1
        else:
            dic[(ABC_list[i][0], ABC_list[i][1])] = 1

for i in dic.values():
    if i >= 2:
        Sum += ((N - i) * (i * (i - 1) // 2) + i * (i - 1) * (i - 2) // 6) % 1000000007
result = (N * (N - 1) * (N - 2) // 6 - Sum) % 1000000007
print(result)