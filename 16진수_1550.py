X = input()
num_list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
dic1 = {i: i for i in range(10)}
dic2 = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15}
Sum = 0
for i in range(len(X)):
    if X[i] in num_list:
        Sum += dic1[int(X[i])] * 16**(len(X) - i - 1)
    else:
        Sum += dic2[X[i]] * 16**(len(X) - i - 1)
print(Sum)