dic = {1:0, 2:1, 3:1, 4:2, 5:2}


def P(N):
    if N in dic:
        return dic[N]
    else:
        result = P(N-1) + P(N-5)
        dic[N] = result
        return result


T = int(input())
for i in range(0, T):
    N = int(input())
    print(P(N))
