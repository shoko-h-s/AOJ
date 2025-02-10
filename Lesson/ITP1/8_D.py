# リング

s = input()
p = input()

# sを2つ繋ぎ合わせ、途切れた部分の並びがわかるようにする
s_2 = s * 2

if p in s_2:
    print("Yes")
else:
    print("No")
