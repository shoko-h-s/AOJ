# 三角形

import math

a, b, cd = map(int, input().split())

# 角度をラジアンに変換
# 度数よりラジアンで計算した方が、誤差が出にくい?
crd = math.radians(cd)

# 正弦定理を用いて、面積を求める
s = 1/2 * a * b * math.sin(crd)

# 余弦定理を用いて、残りの1辺を求める
c_2 = a**2 + b**2 - 2 * a * b * math.cos(crd)
c = math.sqrt(c_2)

# 周の長さ
l = a + b + c

# 求めた面積を用いて、高さを求める
h = 2 * s / a

print(s)
print(l)
print(h)

# 別解
# ヘロンの公式を用いて、面積を求める
# s_m = (a + b + c) / 2
# s = math.sqrt(s_m * (s_m-a) * (s_m-b) * (s_m-c))
