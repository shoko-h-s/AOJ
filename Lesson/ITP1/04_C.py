# 計算機

cal_list = []
    
while True:
    a, op, b = input().split()

    if op == "?":
        break

    a = int(a)
    b = int(b)
    
    if op == "+":
        result = a + b
    elif op == "-":
        result = a - b
    elif op == "*":
        result = a * b
    else:
        result = a // b

    cal_list.append(result)
    
for cal in cal_list:
    print(cal)

# 解いたChallenge
# JOI Prelim 0588
