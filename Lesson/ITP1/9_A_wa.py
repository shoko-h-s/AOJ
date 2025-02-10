# 単語の検索

# 大文字小文字を区別しない → すべて大文字に統一して判定する
w = input().upper()

counter = 0

while True:
    t = input()
    
    if t == "END_OF_TEXT":
        break
    
    t = t.upper()
    counter += t.count(w)
    
print(counter)

# #3 で wa、カウントが合わないが原因不明
