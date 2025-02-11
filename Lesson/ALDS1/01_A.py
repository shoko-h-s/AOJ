# 挿入ソート

n = int(input())
list_1 = list(map(int, input().split()))

print(" ".join(map(str, list_1)))

for i in range(1, n):
    v = list_1[i]
    j = i - 1

    while (j >= 0) and (list_1[j] > v):
        list_1[j+1] = list_1[j]
        j -= 1

    list_1[j+1] = v

    print(" ".join(map(str, list_1)))
