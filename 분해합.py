N = int(input())
check = 0
for i in range(N):
    Sum = 0
    a = list(str(i))
    for j in range(len(a)):
       Sum += int(a[j])
    if Sum + i == N:
        print(i)
        check = 1
        break
if check == 0:
    print(0)