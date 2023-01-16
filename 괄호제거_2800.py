import sys
from itertools import combinations

line = sys.stdin.readline().strip()
my_list = []
pair = []

for idx, c in enumerate(line):
    if c == '(':
        my_list.append(idx)
    if c == ')':
        x = my_list.pop()
        pair.append((x, idx))

Combi = []
for i in range(1, len(pair) + 1):
    L = list(combinations(pair, i))
    for j in range(len(L)):
        Combi.append(L[j])

result = []
while Combi:
    X = Combi.pop()
    L = []
    for i in range(len(X)):
        L.append(X[i][0])
        L.append(X[i][1])
    L.sort()
    start, end = L[0], L[-1]
    str = line[:start]
    for j in L:
        str += line[start + 1:j]
        start = j
    str += line[end + 1 :]
    result.append(str)

result = list(set(result))
result.sort()

for i in range(len(result)):
    print(result[i])