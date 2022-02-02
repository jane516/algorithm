N = int(input())
N1 = ['2', '3', '5', '7']
prime = ['1', '3', '7', '9']


def find(num):
    for i in range(2, int(int(num)**0.5)+1):
        if int(num) % i == 0:
            return
    if len(num) == N:
        print(num)
    for j in prime:
        find(num+j)

for k in N1:
    find(k)
