import sys


def is_prime(n):
    if n == 1:
        return False
    m = int(n ** 0.5)+1
    for i in range(2, m):
        if (n % i) == 0:
            return False
    return True


def 소인수분해(n):
    A = []
    for i in range(2, int(n**0.5)):
        if n % i == 0:
            while n % i == 0:
                A.append(i)
                n //= i
    if n > 1:
        A.append(n)
    return A


case = sys.stdin.readline().strip()
N = int(case)
if is_prime(N):
    print(-1)
else:
    my_list = 소인수분해(N)
    printer = []
    for even, odd in zip(my_list[::2], my_list[1::2]):
        printer.append(even * odd)

    if len(my_list) == 1:
        print(my_list[0])
    elif len(my_list) % 2 != 0:
        printer[-1] *= my_list[-1]

    for i in range(len(printer)):
        print(printer[i], end=' ')