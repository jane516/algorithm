import sys
N = int(sys.stdin.readline().strip())
case1 = sys.stdin.readline().strip().split()
dic = {}
for i in range(N):
    if case1[i] in dic:
        dic[case1[i]] += 1
    else:
        dic[case1[i]] = 1
M = int(sys.stdin.readline().strip())
case2 = sys.stdin.readline().strip().split()
result = []
for i in range(M):
    if case2[i] in dic:
        result.append(dic[case2[i]])
    else:
        result.append('0')
print(*result)