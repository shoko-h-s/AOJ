# ITP1_2_A Challenge
# 買い物

m, f, b = map(int, input().split())

if m >= b:
    print(0)
elif m + f >= b:
    print(b - m)
else:
    print("NA")
