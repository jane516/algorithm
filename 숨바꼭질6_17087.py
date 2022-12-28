import sys

N, S = map(int, sys.stdin.readline().strip().split())
A_list = list(map(int, sys.stdin.readline().strip().split()))
A_list.append(S)
B_set = set()

for i in range(1, N + 1):
    B_set.add(abs(A_list[i] - A_list[i - 1]))

B_list = list(B_set)


def gcd(a, b):
    a, b = max(a, b), min(a, b)
    r = 1
    while r > 0:
        r = a % b
        a, b = b, r
    return a


a = B_list[0]
for b in B_list:
    a = gcd(a, b)

print(a)