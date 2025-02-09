# 2つの数の交換

xy_list = []
    
while True:
    x, y = map(int, input().split())

    if (x == 0) and (y == 0):
        break

    if x > y:
        x, y = y, x

    xy_list.append([x, y])
    
for xy in xy_list:
    print(xy[0], xy[1])
