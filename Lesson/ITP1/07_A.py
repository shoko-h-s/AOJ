# 成績

grade_list = []

while True:
    m, f, r = map(int, input().split())

    if (m == -1) and (f == -1) and (r == -1):
        break
        
    elif (m == -1) or (f == -1):
        grade = "F"
        
    elif m + f >= 80:
        grade = "A"
        
    elif m + f >= 65:
        grade = "B"
        
    elif m + f >= 50:
        grade = "C"
        
    elif m + f >= 30:
        if r >= 50:
            grade = "C"
        else:
            grade = "D"
            
    else:
        grade = "F"
        
    grade_list.append(grade)
    
for g in grade_list:
    print(g)
