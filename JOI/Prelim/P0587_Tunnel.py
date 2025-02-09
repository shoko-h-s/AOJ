# ITP1_3_D Challenge
# Tunnel

n = int(input())
m = int(input())
io_list = [list(map(int, input().split())) for _ in range(n)]

success = True

# 最大値を m で初期化
max_s = m

for io in io_list:
    m = m + io[0] - io[1]
    
    if m < 0:
        print(0)
        success = False
        break
    
    if m > max_s:
        max_s = m
        
if success:
    print(max_s)
