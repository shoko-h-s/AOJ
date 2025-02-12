# スタック
# 逆ポーランド記法

stack = []

# 要素の追加
def s_push(x):
    stack.append(x)

def s_plus():
    # 別途、アキュムレータ（計算機）用の変数を準備
    acc = stack[-1]
    stack.pop()
    acc += stack[-1]
    stack.pop()
    stack.append(acc)
    
def s_minus():
    acc = stack[-1]
    stack.pop()
    acc = stack[-1] - acc
    stack.pop()
    stack.append(acc)
    
def s_multi():
    acc = stack[-1]
    stack.pop()
    acc *= stack[-1]
    stack.pop()
    stack.append(acc)

a_list = input().split()

for a in a_list:
    
    # 数値である場合
    if a.isdigit():
        s_push(int(a))
        
    elif a == "+":
        s_plus()
        
    elif a == "-":
        s_minus()
        
    elif a == "*":
        s_multi()
        
print(stack[0])


# その他スタックの機能
# 要素を取り出す（今回の実装では使っていない）
# def s_pop():
#    return stack.pop()
