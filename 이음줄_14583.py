H, V = map(float, input().split())
A = (H**2 + V**2)**0.5
넓이 = H * (A**2 - H * A)/(2*V)
세로 = ((A**2 - H*A)/2)**0.5
가로 = 넓이/세로
print(round(가로,2), round(세로,2))