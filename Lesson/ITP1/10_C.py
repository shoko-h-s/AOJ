# 標準偏差

import math

d_list = []

while True:
    n = int(input())

    if n == 0:
        break

    s_list = list(map(int, input().split()))

    # 平均値
    m = sum(s_list) / n

    # 偏差2乗リスト
    s_d = [(s-m)**2 for s in s_list]

    # 偏差2乗和
    ss = sum(s_d)

    # 標準偏差
    s_d = math.sqrt(ss / n)
    
    d_list.append(s_d)
    continue

for d in d_list:
    print(d)

# 偏差：各データの値と平均値の差
# 偏差2乗和：各データの偏差2乗をすべて足した値。データ全体で平均値からどのくらいずれているかを表す。
# 分散：偏差2乗の平均値。各データが平均値からどのくらいずれているかを表す。
# 標準偏差：分散の正の平方根。元の変数と同じ尺度に直している。
