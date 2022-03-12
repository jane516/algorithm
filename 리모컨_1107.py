import sys
N = int(sys.stdin.readline().strip())
M = int(input())
if M:
    case = sys.stdin.readline().strip().split()
check_list = []
for i in range(M):
    check_list.append(int(case[i]))
Min = abs(N - 100)
for i in range(1000001):
    i = str(i)
    for j in range(len(i)):
        if int(i[j]) in check_list:
            break
        elif j == len(i) - 1:
            Min = min(Min, abs(int(i) - N) + len(i))
print(Min)