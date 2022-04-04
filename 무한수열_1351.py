import sys
case = sys.stdin.readline().strip().split()
N, P, Q = int(case[0]), int(case[1]), int(case[2])
dic = {0: 1}


def A(n):
    if n in dic:
        return dic[n]
    else:
        dic[n] = A(n//P) + A(n//Q)
        return dic[n]


print(A(N))