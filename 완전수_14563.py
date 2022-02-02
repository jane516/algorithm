import sys
T = int(input())
case = sys.stdin.readline().strip().split()
A = [0] * T
for i in range(T):
    A[i] = int(case[i])


def 완전수(n):
    if n == 1:
        약수 = [0]
    else:
        약수 = [1]
        for i in range(2, int(n ** 0.5) + 1):
            if i ** 2 == n:
                약수.append(i)
            elif n % i == 0:
                약수.append(i)
                약수.append(n // i)
    if sum(약수) == n:
        return 0
    elif sum(약수) < n:
        return -1
    else:
        return 1


for k in A:
    if 완전수(k) == 0:
        print('Perfect')
    elif 완전수(k) == -1:
        print('Deficient')
    else:
        print('Abundant')