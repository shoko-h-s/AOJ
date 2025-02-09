# ITP1_1_D Challenge
# 合計時間 (Total Time)

t_list = [int(input()) for _ in range(4)]

t_sum = sum(t_list)

minutes = t_sum // 60
seconds = t_sum % 60

print(minutes)
print(seconds)
