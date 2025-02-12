# 選択ソート

n = int(input())
list_1 = list(map(int, input().split()))

count = 0

for i in range(n):
    min_j = i

    for j in range(i, n):
        if list_1[j] < list_1[min_j]:
            min_j = j

    if i != min_j:
        list_1[i], list_1[min_j] = list_1[min_j], list_1[i]
        count += 1

print(" ".join(map(str, list_1)))
print(count)
