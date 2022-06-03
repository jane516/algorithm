N = 123
linked = [[0 for _ in range(N + 1)] for _ in range(N + 1)]
line = [(1, 2), (1, 10), (1, 3), (2, 16), (16, 19), (10, 18), (11, 18), (18, 19), (3, 14), (14, 15),
        (15, 39), (39, 40), (4, 5), (5, 6), (6, 7), (6, 8), (8, 9), (9, 26), (9, 27), (9, 24),
        (24, 25), (6, 33), (33, 34), (34, 35), (35, 36), (36, 37), (37, 38), (25, 41), (38, 41), (38, 83),
        (83, 84), (84, 85), (41, 62), (62, 63), (12, 13), (13, 43), (41, 43), (41, 42), (42, 78), (78, 79),
        (78, 80), (42, 68), (42, 69), (68, 70), (69, 70), (38, 64), (64, 65), (65, 66), (66, 67), (67, 69),
        (67, 68), (3, 71), (3, 72), (71, 73), (72, 73), (73, 74), (44, 45), (10, 45), (45, 46), (19, 51),
        (17, 51), (51, 52), (11, 45), (11, 47), (47, 48), (48, 51), (48, 49), (49, 50), (50, 53),
        (53, 54), (54, 55), (55, 56), (56, 57), (54, 75), (75, 76), (76, 77), (77, 81), (81, 82), (10, 82),
        (30, 81), (28, 53), (28, 29), (29, 30), (29, 31), (31, 32), (20, 21), (20, 22), (21, 23), (22, 23),
        (23, 58), (55, 58), (58, 59), (58, 60), (59, 61), (60, 61), (40, 86), (46, 86), (32, 86), (86, 87),
        (77, 88), (88, 89), (88, 95), (89, 93), (74, 93), (93, 94), (94, 104), (95, 96), (96, 97), (97, 99),
        (40, 98), (98, 99), (99, 100), (97, 114), (96, 117), (78, 90), (85, 90), (90, 91), (84, 92), (85, 101),
        (101, 102), (102, 103), (70, 103), (111, 112), (112, 113), (114, 115), (115, 116), (104, 105), (105, 106), (105, 116),
        (106, 107), (107, 108), (108, 109), (108, 110), (108, 117), (63, 117), (117, 118), (118, 120), (118, 122), (118, 123),
        (118, 119), (70, 118), (91, 120), (92, 122), (120, 121), (31, 81), (30, 93), (9, 36), (54, 87), (56, 61), (29, 96),
        (12, 79), (12, 80)]


def matrix_multi(arr1, arr2):
    result = [[0 for _ in range(len(arr2[0]))] for _ in range(len(arr1))]
    for i in range(len(arr1)):
        for j in range(len(arr2[0])):
            for k in range(len(arr1[0])):
                result[i][j] += (arr1[i][k] * arr2[k][j])
    return result


def power(Matrix, n):
    if n == 1:
        return Matrix
    else:
        if n % 2 == 0:
            temp = power(Matrix, n // 2)
            return matrix_multi(temp, temp)
        else:
            temp = power(Matrix, n-1)
            return matrix_multi(temp, Matrix)


for i in line:
    a, b = i[0], i[1]
    linked[a][b] = 1


cnt = 0
M = []
for k in range(2, 123):
    S = power(linked, k)
    for i in range(N + 1):
        for j in range(N + 1):
            if linked[i][j] == 1 and S[i][j] != 0:
                cnt += 1
                M.append([i, j])

cnt2 = 0
for i in range(N + 1):
    cnt2 += linked[i].count(1)
print(len(line))
print(cnt2)
print(cnt)
print(M)


