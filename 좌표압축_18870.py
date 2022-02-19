import sys
N = int(sys.stdin.readline().strip())
case = sys.stdin.readline().strip().split()
X_list = [0 for _ in range(N)]
for i in range(N):
    X_list[i] = int(case[i])
my_list = list(set(X_list))
my_list.sort()
dic = {my_list[i]: i for i in range(len(my_list))}
for i in X_list:
    print(dic[i], end=' ')
