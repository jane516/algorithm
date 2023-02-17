import sys
from pprint import pprint

sys.setrecursionlimit(10000)
input = sys.stdin.readline

N = int(input().strip())


def is_square_valid(arr, x, y, n):
    x_start = ((x-1) // 3) * 3 + 1
    y_start = ((y-1) // 3) * 3 + 1

    for i in range(x_start, x_start + 3):
        for j in range(y_start, y_start + 3):
            if arr[i][j] == n:
                return False
    return True


def is_vertical_valid(arr, x, y, n):
    for i in range(1, 10):
        if arr[i][y] == n:
            return False
    return True


def is_horizontal_valid(arr, x, y, n):
    for i in range(1, 10):
        if arr[x][i] == n:
            return False
    return True


def find(arr, remains, cnt):
    global found

    if cnt == 5:
        found = True
        return arr

    for j in range(cnt, 5):
        x, y = remains[j]

        for i in range(1, 10):
            if not is_vertical_valid(arr, x, y, i):
                continue
            if not is_horizontal_valid(arr, x, y, i):
                continue
            if not is_square_valid(arr, x, y, i):
                continue
            arr[x][y] = i
            cnt += 1
            if result := find(arr, remains, cnt):
                return result
            arr[x][y] = 0
            cnt -= 1


for _ in range(N):
    boards = [[0 for _ in range(10)] for _ in range(10)]
    zeros = []
    for i in range(9):
        for j, c in enumerate(input().strip()):
            num = int(c)
            if num == 0:
                zeros.append((i+1, j+1))
            boards[i+1][j+1] = num
    found = False
    find(boards, zeros, 0)
    if found:
        for i in range(1, 10):
            Sum1, Sum2, Sum3 = 0, 0, 0
            for j in range(1, 10):
                Sum1 += boards[i][j]
                Sum2 += boards[j][i]
            for k in range(3):
                for l in range(3):
                    Sum3 += boards[((i-1)//3)*3+1+k][((i-1)%3)*3+l+1]
            if Sum1 != 45 or Sum2 != 45 or Sum3 != 45:
                found = False
    if found:
        for i in range(9):
            for j in range(9):
                print(boards[i+1][j+1], end='')
            print()
    else:
        print("Could not complete this grid.")
    print()