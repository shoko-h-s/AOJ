# ITP1_2_A Challenge
# 電子レンジ (Microwave)

a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())

if a < 0:
    melting = abs(a) * c + d
    warming = b * e
    print(melting + warming)
    
elif a == 0:
    warming = d + b * e
    print(warming)
    
else:
    temp = b - a
    print(e * temp)
