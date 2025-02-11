# 不足しているカードの発見

# トランプ一式を表すリストを宣言
playing_cards = [[i+1 for i in range(13)] for j in range(4)]
mark_list = ["S", "H", "C", "D"]

n = int(input())
card_list = [input() for _ in range(n)]

for card in card_list:
    mark, num = card.split()
    num = int(num)
    
    if mark == "S":
        playing_cards[0].remove(num)
        
    elif mark == "H":
        playing_cards[1].remove(num)
        
    elif mark == "C":
        playing_cards[2].remove(num)
        
    else:
        playing_cards[3].remove(num)
        
for i in range(4):
    for j in range(len(playing_cards[i])):
        print(mark_list[i] + " " + str(playing_cards[i][j]))

# for 文を使ったリスト内包表記で2次元配列を作成・初期化することができる
# 変数名 = [[初期値 for i in range(横方向のサイズ)] for j in range(縦方向のサイズ)]
