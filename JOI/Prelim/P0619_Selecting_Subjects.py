# ITP1_2_C Challenge
# 科目選択 (Selecting Subjects)

abcd_list = [int(input()) for _ in range(4)]
ef_list = [int(input()) for _ in range(2)]

test_1 = sum(abcd_list) - min(abcd_list)
test_2 = max(ef_list)

print(test_1 + test_2)
