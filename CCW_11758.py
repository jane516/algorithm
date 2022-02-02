def cross_product(x1, y1, x2, y2, x3, y3):
    answer = 0
    P = x1 * y2 + x2 * y3 + x3 * y1
    M = x2 * y1 + x3 * y2 + x1 * y3
    if P - M < 0:
        answer = -1
    elif P - M == 0:
        answer = 0
    else:
        answer = 1
    return answer


x1, y1 = map(int, input().split())
x2, y2 = map(int, input().split())
x3, y3 = map(int, input().split())
print(cross_product(x1, y1, x2, y2, x3, y3))