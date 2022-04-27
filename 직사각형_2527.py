import sys


def 직사각형(x1, y1, p1, q1, x2, y2, p2, q2):
    A, B = [0, 0, 0, 0], [0, 0, 0, 0]
    if min(x1, x2) == x1:
        A = [x1, y1, p1, q1]
        B = [x2, y2, p2, q2]
    else:
        A = [x2, y2, p2, q2]
        B = [x1, y1, p1, q1]
    if A[2] < B[0] or A[3] < B[1] or A[1] > B[3]:
        return 'd'
    elif A[2] == B[0]:
        if A[3] == B[1] or A[1] == B[3]:
            return 'c'
        else:
            return 'b'
    elif A[3] == B[1] or A[1] == B[3]:
        return 'b'
    else:
        return 'a'


result = []
for i in range(4):
    x1, y1, p1, q1, x2, y2, p2, q2 = map(int, sys.stdin.readline().strip().split())
    result.append(직사각형(x1, y1, p1, q1, x2, y2, p2, q2))
for i in range(4):
    print(result[i])