# 長方形の描画

hw_list = []

while True:
    h, w = map(int, input().split())
    
    if (h == 0) and (w == 0):
        break

    hw_list.append([h, w])

for hw in hw_list:
    for i in range(hw[0]):
        print("#" * hw[1])
    
    print()
