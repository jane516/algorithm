import sys
case = sys.stdin.readline().strip().split()
A, B = int(case[0]), int(case[1])
count = 0
check = 0
while True:
    if A == B:
        break
    elif B < A:
        check = 1
        break
    if B % 2 == 0:
        B //= 2
        count += 1
    elif B % 10 == 1:
        B //= 10
        count += 1
    else:
        check = 1
        break
if check == 1:
    print(-1)
else:
    print(count + 1)



