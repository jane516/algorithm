import sys

K = int(sys.stdin.readline().strip())
dic = {1: 0, 2: 0, 3: 0, 4: 0}
W, H = 0, 0
len_list1 = [0, 0, 0, 0, 0]
len_list2 = []
cnt = 0
for _ in range(6):
    dir, dist = map(int, sys.stdin.readline().strip().split())
    dic[dir] += 1
    len_list1[dir] += dist
    len_list2.append([dir, dist])

S1 = 1
for key in dic:
    if dic[key] == 1:
        S1 *= len_list1[key]

idx_list = []
for i in range(6):
    if dic[len_list2[i][0]] == 2:
        idx_list.append(i)

idx_list.sort()
idx1, idx2, idx3, idx4 = idx_list
S2 = 1
if idx4 - idx1 == 3:
    S2 = len_list2[idx2][1] * len_list2[idx3][1]
else:
    if idx2 == 1:
        S2 *= len_list2[idx1][1]
    else:
        S2 *= len_list2[idx3][1]
    if idx3 == 2:
        S2 *= len_list2[idx2][1]
    else:
        S2 *= len_list2[idx4][1]

print((S1 - S2) * K)