N = int(input())
받을돈 = 1000 - N
coin = [500, 100, 50, 10, 5, 1]
Sum = 0
for i in coin:
    Sum += 받을돈 // i
    받을돈 %= i
print(Sum)