# 素数
# 試し割り法

import math

def isprime(x):
    if x == 2:
        return True
    
    elif (x < 2) or (x % 2 == 0):
        return False
    
    # 3以上の奇数のみを調べる
    i = 3

    while i <= math.sqrt(x):
        if x % i == 0:
            return False
        
        i += 2

    return True


n = int(input())
a_list = [int(input()) for _ in range(n)]

answers = [isprime(a) for a in a_list]

print(sum(answers))
