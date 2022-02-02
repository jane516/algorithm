import sys
case = list(sys.stdin.readline().strip())
count = 0
for i in range(1, len(case)):
    if case[i] != case[i-1]:
        count += 1
if count % 2 == 0:
    print(count // 2)
else:
    print(count // 2 + 1)