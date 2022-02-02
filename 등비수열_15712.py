import sys


def power(a, n, mod):
    if n == 1:
        return a
    else:
        t = power(a, n // 2, mod)
        if n % 2 == 0:
            return t * t % mod
        else:
            return t * t * a % mod


def 등비수열합(a, r, n, mod):
    if n == 1:
        return a
    else:
        s = 등비수열합(a, r, n // 2, mod)
        if n % 2 == 0:
            return s * (1 + power(r, n // 2, mod)) % mod
        else:
            return s * (1 + power(r, n // 2, mod)) % mod + a * power(r, n - 1, mod) % mod


case = sys.stdin.readline().strip()
a = int(case.split()[0])
r = int(case.split()[1])
n = int(case.split()[2])
mod = int(case.split()[3])
print(등비수열합(a, r, n, mod) % mod)


