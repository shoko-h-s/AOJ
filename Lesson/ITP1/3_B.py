# テストケースの出力

# データセット格納の準備
x_list = []
i = 1

while True:
    x = int(input())
    
    if x == 0:
        break
        
    x_list.append(x)
    
for i in range(len(x_list)):
    print(f"Case {i+1}: {x_list[i]}")

# 未回答のChallenge
# JOI Prelim 0582
