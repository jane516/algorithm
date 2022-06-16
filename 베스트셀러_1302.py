import sys

N = int(sys.stdin.readline().strip())
dic = {}
my_list = []
for _ in range(N):
    book = sys.stdin.readline().strip()
    if book in dic:
        dic[book] += 1
    else:
        dic[book] = 1
M = 0
for book in dic:
    M = max(M, dic[book])
for book in dic:
    if dic[book] == M:
        my_list.append(book)
my_list.sort()
print(my_list[0])