# ITP1_7_B Challenge
# 被験者の選定

import itertools

results = []

while True:
    n = int(input())
    
    if n == 0:
        break
        
    a_list = list(map(int, input().split()))
    
    d_min = 1000000
    
    for a in itertools.combinations(a_list, 2):
        d = abs(a[0] - a[1])
        if d < d_min:
            d_min = d
            
    results.append(d_min)
        
for r in results:
    print(r)
