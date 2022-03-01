value = {'black': 0, 'brown': 1, 'red': 2, 'orange': 3, 'yellow': 4,
         'green': 5, 'blue': 6, 'violet': 7, 'grey': 8, 'white': 9}
multi = {'black': 1, 'brown': 10, 'red': 10**2, 'orange': 10**3, 'yellow': 10**4,
         'green': 10**5, 'blue': 10**6, 'violet': 10**7, 'grey': 10**8, 'white': 10**9}
value1 = input()
value2 = input()
multi1 = input()
result = (value.get(value1) * 10 + value.get(value2)) * multi.get(multi1)
print(result)