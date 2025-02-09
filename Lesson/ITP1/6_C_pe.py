# ITP1_6_C
# 公舎の入居者数

# 3次元配列を宣言する
apart_list = [[[0 for i in range(10)] for j in range(3)] for k in range(4)]

n = int(input())
bfrv_list = [input() for _ in range(n)]

for bfrv in bfrv_list:
    b, f, r, v = map(int, bfrv.split())
    
    apart_list[b-1][f-1][r-1] += v
        
for i in range(4):
    for j in range(3):
        print(" ".join(map(str, apart_list[i][j])))

        if (j == 2) and (i != 3):
            print("####################")

# PEエラー、原因不明
