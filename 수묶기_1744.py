N = int(input())
nums = []
pnums = []
mnums = []
Sum = 0
for i in range(N):
    num = int(input())
    if num > 1:
        pnums.append(num)
    elif num < 0:
        mnums.append(num)
    else:
        nums.append(num)
pnums.sort()
mnums.sort()
if len(pnums) % 2 == 0:
    for i in range(len(pnums)-1, -1, -2):
        Sum += pnums[i] * pnums[i-1]
else:
    Sum += pnums[0]
    for i in range(len(pnums)-1, 0, -2):
        Sum += pnums[i] * pnums[i-1]
if len(mnums) % 2 == 0:
    for i in range(0, len(mnums), 2):
        Sum += mnums[i] * mnums[i+1]
else:
    for i in range(0, len(mnums)-1, 2):
        Sum += mnums[i] * mnums[i+1]
    if 0 not in nums:
        Sum += mnums[-1]
Sum += nums.count(1)
print(Sum)