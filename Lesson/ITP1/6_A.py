# 数列の反転

n = int(input())
a_list = list(map(int,input().split()))

a_rev = a_list[::-1]

print(" ".join(map(str, a_rev)))

# 別解（逆順にする方法）
# 1.元のリストを反転して上書きする場合
# a_list.reverse()

# 2.反転済のリストを別途生成する場合
# a_list_reversed = reversed(a_list)
