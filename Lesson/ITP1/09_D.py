# 文字列変換

str = input()
q = int(input())
c_list = [input().split() for _ in range(q)]

for c in c_list:
    if "print" in c[0]:
        a, b = int(c[1]), int(c[2])
        print(str[a:b+1])

    elif "reverse" in c[0]:
        a, b = int(c[1]), int(c[2])

        # 操作する部分としない部分を分ける
        str_f = str[:a]
        str_b = str[b+1:]
        str_c = str[a:b+1]

        str_c = str_c[::-1]

        str = str_f + str_c + str_b

    else:
        a, b, p = int(c[1]), int(c[2]), c[3]

        str_f = str[:a]
        str_b = str[b+1:]

        str = str_f + p + str_b
