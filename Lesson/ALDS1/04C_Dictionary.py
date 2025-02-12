# 辞書

n = int(input())
com_list = [input() for _ in range(n)]

# 集合を使い高速化する
dic = set()

for com in com_list:
    if "insert" in com:
        c, str = com.split()
        
        # 集合に要素を追加する場合は、addメソッド
        dic.add(str)

    else:
        c, str = com.split()
        
        if str in dic:
            print("yes")
        else:
            print("no")
