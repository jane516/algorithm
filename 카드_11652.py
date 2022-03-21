import sys
N = int(sys.stdin.readline().strip())
dic = {}
for i in range(N):
    case1 = sys.stdin.readline().strip()
    if case1 in dic:
        dic[case1] += 1
    else:
        dic[case1] = 1

result = []
Max = max(dic.values())
for key, value in dic.items():
    if value == Max:
        result.append(int(key))
print(min(result))