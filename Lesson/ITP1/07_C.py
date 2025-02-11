# 表計算

r, c = map(int, input().split())
table = [list(map(int, input().split())) for _ in range(r)]

# 各行の合計値を追加する
for t in table:
    sum_r = sum(t)
    t.append(sum_r)

# 各列の合計値の行を追加
totals = []
    
for i in range(c):
    total = 0
    
    for j in range(r):
        total += table[j][i]
        
    totals.append(total)
    
sum_t = sum(totals)
totals.append(sum_t)
        
for i in range(r):
    print(" ".join(map(str, table[i])))
    
print(" ".join(map(str, totals)))
