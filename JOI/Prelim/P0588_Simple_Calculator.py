# ITP1_4_C Challenge
# Simple Calculator

# 計算結果を格納するリスト
cal_list = []

while True:
    a = input()
    
    if a == "=":
        break

    elif a.isdigit():
        cal_list.append(a)

        # 挿入後の cal_list が数字1つでなければ
        if len(cal_list) != 1:
            s = "".join(cal_list)
            
            # 計算結果を文字列型で変数に入れる
            result = str(eval(s))
            
            # 計算結果の代入前に、計算が終わった分の数字・演算子を削除する
            cal_list = []
            
            cal_list.append(result)
            
    elif a == "/":
        cal_list.append("//")

    else:
        cal_list.append(a)

print(cal_list[0])
