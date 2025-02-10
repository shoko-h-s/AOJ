# 数字の和

numbers = []

while True:
    x = list(input())
    
    if x == ["0"]:
        break
        
    x_list = [int(i) for i in x]
    numbers.append(sum(x_list))

for n in numbers:
    print(n)
