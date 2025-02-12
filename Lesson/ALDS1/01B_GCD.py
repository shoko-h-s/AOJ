# 最大公約数
# ユークリッドの互除法を用いる

x, y = map(int, input().split())

while (x != 0) and (y != 0):
    if x < y:
        y %= x
    else:
        x %= y

if x == 0:
    gcd = y
else:
    gcd = x
    
print(gcd)
