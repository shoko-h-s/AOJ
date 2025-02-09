# ITP1_5_B Challenge
# 旗を作ろう

w, h, c = input().split()

w = int(w)
h = int(h)

for i in range(1, h+1):
    
    # 1行目と最終行
    if (i == 1) or (i == h):
        mid_s = "-" * (w-2)
        print(f"+{mid_s}+")
    
    # 中央行
    elif i == h // 2 + 1:
        mid_s = "." * ((w-3) // 2)
        print(f"|{mid_s}{c}{mid_s}|")
        
    else:
        mid_s = "." * (w-2)
        print(f"|{mid_s}|")
