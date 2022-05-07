import sys

n = int(sys.stdin.readline().strip())
N_list = {}
result = []
for i in range(n):
    name, el = sys.stdin.readline().strip().split()
    if name in N_list:
        N_list[name] = el
    else:
        N_list[name] = el
for name in N_list.keys():
    if N_list[name] == 'enter':
        result.append(name)
result.sort()
for i in range(len(result)):
    print(result[-1-i])