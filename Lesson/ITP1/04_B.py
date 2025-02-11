# 円の面積と円周

import math

r = float(input())

# mathモジュールより、円周率 π を参照できる pi 定数を使う
area = r * r * math.pi
long = r * 2 * math.pi

print(area, long)
