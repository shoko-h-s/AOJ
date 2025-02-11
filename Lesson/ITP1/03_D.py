# ITP1_3_D
# 約数の数

a, b, c = map(int, input().split())

i = a
counter = 0

while i <= b:
    if c % i == 0:
        counter += 1
        
    i += 1
    
print(counter)

# 解いたChallenge
# JOI Prelim 0587

# 未回答のChallenge
# PCK Prelim 0278
