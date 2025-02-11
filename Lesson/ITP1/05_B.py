# フレームの描画

hw_list = []

while True:
    h, w = map(int, input().split())
    
    if (h == 0) and (w == 0):
        break

    hw_list.append([h, w])
    
for hw in hw_list:
    h, w = hw[0], hw[1]
    
    for i in range(1, h+1):
        
        # 1行目と最終行
        if (i == 1) or (i == h):
            print("#" * w)
            
        else:
            mid_s = "." * (w-2)
            print(f"#{mid_s}#")            
            
    print()

# 解いたChallenge
# PCK Final 0368
