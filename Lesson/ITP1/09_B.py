# シャッフル

cards = []

while True:
    string = input()
    if string == "-":
        break

    m = int(input())
    
    h_list = [int(input()) for _ in range(m)]

    for h in h_list:
        string = string[h:] + string[:h]

    cards.append(string)
    
for c in cards:
    print(c)
