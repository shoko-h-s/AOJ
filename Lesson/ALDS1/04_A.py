# 線形探索

n = int(input())
s_list = list(map(int, input().split()))
q = int(input())
t_list = list(map(int, input().split()))

count = 0

for t in t_list:

    i = 0

    # 番兵
    # 探すべき値をリストの最後尾に追加
    # より簡潔に記述できる
    s_list.append(t)

    while i != n:
        if t == s_list[i]:
            count += 1
            break
            
        i += 1
            
    # 各ループ終了時に番兵をリセットする
    s_list.pop()

print(count)
