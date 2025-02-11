# チェスボードの描画

hw_list = []

while True:
    h, w = map(int, input().split())
    
    if (h == 0) and (w == 0):
        break

    hw_list.append([h, w])
    
for hw in hw_list:
    h, w = hw[0], hw[1]
    
    for i in range(1, h+1):
        
        # 奇数行
        if i % 2 == 1:
        
            # "#."のセットを作る
            sd = "#." * (w // 2 - 1)

            if w % 2 == 0:
                print(sd + "#.")
            
            # w = 3の時のみ例外処理が必要
            elif w == 3:
                print("#.#")
                
            else:
                print(sd + "#")
        
        # 偶数行
        else:
            # ".#"のセットを作る
            sd = ".#" * (w // 2 - 1)
            
            if w % 2 == 0:
                print(sd + ".#")
                
            # w = 3の時のみ例外処理が必要
            elif w == 3:
                print(".#.")
                
            else:
                print(sd + ".")
                
    print()

# #3 で wa、見た目は合っていて原因不明
