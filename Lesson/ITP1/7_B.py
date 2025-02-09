# 組み合わせの数

import itertools

results = []

while True:
    counter = 0    
    n, x = map(int, input().split())

    if (n == 0) and (x == 0):
        break
        
    # 1～nまでの数値のリストを作る
    numbers = [i+1 for i in range(n)]
    
    # 組み合わせを列挙する
    for a in itertools.combinations(numbers, 3):
        if sum(a) == x:
            counter += 1
            
    results.append(counter)
        
for r in results:
    print(r)
    
# 解いたChallenge
# ICPC Prelim 1608
