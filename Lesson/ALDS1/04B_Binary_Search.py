# 二分探索

n = int(input())
s_list = list(map(int, input().split()))
q = int(input())
t_list = list(map(int, input().split()))

count = 0

for t in t_list:

    # 両端の値を初期化
    left = 0
    right = n - 1

    while left <= right:

        # 探索範囲の中央
        mid = (left + right) // 2
        
        if s_list[mid] == t:
            count += 1
            break

        elif s_list[mid] < t:
            left = mid + 1

        else:
            right = mid - 1
            
print(count)
