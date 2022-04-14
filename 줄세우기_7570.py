import sys
N = int(sys.stdin.readline().strip())
case = sys.stdin.readline().strip().split()
case_list = [int(case[i]) - 1 for i in range(N)]
index_list = [0 for _ in range(N)]
for i in range(N):
    index_list[case_list[i]] = i
M = 0
cnt = 1
for i in range(N-1):
    if index_list[i] < index_list[i+1]:
        cnt += 1
        if M < cnt:
            M = cnt
    else:
        cnt = 1
print(N - M)