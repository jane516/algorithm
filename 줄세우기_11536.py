import sys
N = int(input())
name_list = []
for i in range(N):
    name = sys.stdin.readline().strip()
    name_list.append(name)
A = name_list[:]
A.sort()
B = A[:]
B.reverse()
if name_list == A:
    print('INCREASING')
elif name_list == B:
    print('DECREASING')
else:
    print('NEITHER')