import sys
case = sys.stdin.readline().strip()
A = int(case.split()[0])
B = int(case.split()[1])
A_list = list(bin(A)[2:])
B_list = list(bin(B)[2:])
Sum1 = Sum2 = 0
l1 = len(A_list)
l2 = len(B_list)
i = 1
for i in range(1, 2 ** (l1-1) + 1, i * 2):
    Sum1 += 2 ** (i-1) * (A // (2 ** i))
for i in range(1, 2 ** (l2-1) + 1, i * 2):
    Sum2 += 2 ** (i-1) * (B // (2 ** i))
print(Sum2 + B - Sum1 - A)