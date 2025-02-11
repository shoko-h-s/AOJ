# ベクトルと行列の積
# AOJではNumpyを使うとエラーになる

n, m = map(int, input().split())
a_list = [list(map(int, input().split())) for _ in range(n)]
b_list = [int(input()) for _ in range(m)]

c_list = []

for i in range(n):
    c = 0
    
    for j in range(m):
        c += a_list[i][j] * b_list[j]
        
    c_list.append(c)
    
for c in c_list:
    print(c)
