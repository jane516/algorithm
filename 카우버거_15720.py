import sys
case = sys.stdin.readline().strip().split()
B, C, D = int(case[0]), int(case[1]), int(case[2])
B_list = list(map(int, sys.stdin.readline().strip().split()))
C_list = list(map(int, sys.stdin.readline().strip().split()))
D_list = list(map(int, sys.stdin.readline().strip().split()))
B_list.sort()
C_list.sort()
D_list.sort()
m = min(B, C, D)
Sum = sum(B_list) + sum(C_list) + sum(D_list)
print(Sum)
discount = 0
for i in range(m):
    discount += B_list[-1-i] + C_list[-1-i] + D_list[-1-i]
print(Sum - discount // 10)