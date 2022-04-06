import sys
N = int(sys.stdin.readline().strip())
막대기 = []
count = 0
for i in range(N):
    막대기.append(int(sys.stdin.readline().strip()))
X = 막대기.pop()
while 막대기:
    M = 막대기.pop()
    if M > X:
        X = M
        count += 1
print(count + 1)