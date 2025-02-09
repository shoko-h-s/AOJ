# 割り算

a, b = map(int, input().split())

d = a // b
r = a % b
f = a / b

print(d, r, f)

# 誤差の処理？
# Fractionでの処理も試みたが、同じく #9 で wa
