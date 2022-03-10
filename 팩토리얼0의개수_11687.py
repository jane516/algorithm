import sys
M = int(sys.stdin.readline().strip())


def 영의개수(N):
    count = 0
    i = 5
    while True:
        if N // i == 0:
            break
        count += N // i
        i *= 5
    return count


left, right = 1, 5 * M

while True:
    mid = (left + right) // 2
    if left > right:
        print(-1)
        break
    if 영의개수(mid) == M:
        print(mid - mid % 5)
        break
    elif 영의개수(mid) > M:
        right = mid - 1
    else:
        left = mid + 1