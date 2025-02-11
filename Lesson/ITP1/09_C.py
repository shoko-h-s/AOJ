# カードゲーム

n = int(input())
c_list = [input().split() for _ in range(n)]

t_score = 0
h_score = 0

for c in c_list:
    if c[0] == c[1]:
        t_score += 1
        h_score += 1
    
    else:
        # 降順にソートして、元のリストと一致するかどうかで勝敗を判断する
        c_sorted = sorted(c, reverse=True)
    
        if c == c_sorted:
            t_score += 3
            
        else:
            h_score += 3
            
print(t_score, h_score)

# 比較データが2つなので、比較演算子を使うことも可能
# 辞書で遅い方が、大きいという判定になる
