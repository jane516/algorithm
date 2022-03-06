ha = float(input())
hb = float(input())
hc = float(input())
A = ha * hb
B = hb * hc
C = hc * ha
분모 = (ha * hb * hc) ** 4
분자 = (A + B + C) * (A + B - C) * (A + C - B) * (B + C - A)
result = (분모 / 분자) ** 0.5
print(result)