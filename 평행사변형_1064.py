a = list(map(int, input().split()))
A_x = a[0] - a[2]
A_y = a[1] - a[3]
B_x = a[2] - a[4]
B_y = a[3] - a[5]
C_x = a[4] - a[0]
C_y = a[5] - a[1]
if B_x * C_y == C_x * B_y:
    print(-1)
else:
    length_A = A_x ** 2 + A_y ** 2
    length_B = B_x ** 2 + B_y ** 2
    length_C = C_x ** 2 + C_y ** 2
    length_list = [length_A, length_B, length_C]
    length_list.sort()
    MAX = length_list[2] ** 0.5 + length_list[1] ** 0.5
    MIN = length_list[0] ** 0.5 + length_list[1] ** 0.5
    print(2 * (MAX - MIN))
