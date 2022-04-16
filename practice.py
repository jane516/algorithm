import pandas as pd
import os
from os import read

table = {
    "NUM" : [1, 2, 3, 4],
    "STRING": ["a", "b", "c", "d"],
    "FLOAT": [0.0, 1.0, 2.0, 3.0]
}
df = pd.DataFrame(table)

excel = pd.read_excel("C:/Users/jane/Desktop/test.xlsx")
print(excel)

def add(a, b):
    return a+b

# 함수
def minus(a, b):
    return a-b

# 모듈
def calculator(type, a, b):
    if type == "add":
        return add(a, b)
    if type == "minus":
        return minus(a, b)

print(calculator("add", 5, 10))

def test(a, b, c):
    return c, b, a

print(test(1, 2, 3))
print(test(a=1, b=2, c=3))
print(test(1, 2, c=3))

def defaultfunc(a=5, b=10):
    return a + b

print(defaultfunc(10, 10))
print(defaultfunc(10, 20))
print(defaultfunc(10))
print(defaultfunc())

def many(t, *args, **kwargs):
    print(t, args)
    print(kwargs)
many(1, 2, 3, 4, 5, 6, 7, 8, 9)
many(1, 2, 3, 4, 5, 6, a=7, b=8, c=9)

x = 10
y = 5
def abc():
    global x, y
    x = 20
    y = 15
    print(x)
    print(y)
abc()
print(x)
print(y)