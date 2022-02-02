import sys
case = sys.stdin.readline().strip()
N = int(case)
A = []
while N > 0:
    A.append(N % 3)
    N //= 3
count1 = A.count(1)
count2 = A.count(2)
if count1 == 0 or count2 != 0:
    print('NO')
else:
    print('YES')