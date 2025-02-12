# バブルソート

n = int(input())
list_1 = list(map(int, input().split()))

count = 0
flag = 1

# 未ソート部分の先頭インデックス
i = 0

while flag:
    flag = 0

    for j in range(n-1, i, -1):
        if list_1[j] < list_1[j-1]:
            list_1[j], list_1[j-1] = list_1[j-1], list_1[j]
            flag = 1
            count += 1

    i += 1

print(" ".join(map(str, list_1)))
print(count)
