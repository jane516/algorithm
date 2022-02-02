def gcd(a, b):
    a, b = max(a, b), min(a, b)
    if b == 0:
        return a
    return gcd(b, a % b)


N = int(input())
A = []
B = []
for i in range(N):
    A.append(int(input()))
A.sort()


for i in range(N-1):
    B.append(A[i+1]-A[i])

GCD = B[0]
for i in range(N-2):
    GCD = min(GCD, gcd(B[i], B[i+1]))

result_list = [GCD]
a = GCD
for i in range(2, int(GCD ** 0.5) + 1):
    if GCD % i == 0:
        result_list.append(i)
        if i != a // i:
            result_list.append(a // i)
result_list.sort()

for i in result_list:
    print(i, end=' ')