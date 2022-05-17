import sys
N, S = map(int, sys.stdin.readline().strip().split())
num_list = list(map(int, sys.stdin.readline().strip().split()))
num_list.sort()
start, end = 0, N
Sum = sum(num_list)
count = 0
if S in num_list:
    count += num_list.count(S)
while start < end:
    Sum = sum(num_list[start:end])
    if Sum == S:
        count += 1
        start += 1
        end -= 1
    elif Sum > S:
        start += 1
    else:
        end -= 1
print(count)