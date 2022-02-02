def Combination(n, r, mod):
    if n-r < r:
        r = n - r
    분자 = 분모 = 1
    for i in range(0, r):
        분자 = 분자 * (n - i)
        분모 = 분모 * (r - i)
    return 분자 // 분모 % mod


N, R = map(int, input().split())
M = 1000000007
계수_list1 = []
계수_list2 = []
while N > 0:
    계수_list1.append(N % M)
    계수_list2.append(R % M)
    N //= M
    R //= M
K = 1
for i in range(len(계수_list1)):
    if 계수_list1[i] < 계수_list2[i]:
        K = 0
    else:
        K *= Combination(계수_list1[i], 계수_list2[i], M)
print(K % M)