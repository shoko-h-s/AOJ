# ITP1_1_D Challenge
# カエルはまっすぐ帰る

d, l = map(int, input().split())

big_j = d // l
small_j = d % l

print(big_j + small_j)
