# 距離
# ユークリッド距離

import math

x1, y1, x2, y2 = map(float, input().split())

answer = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

print(answer)
