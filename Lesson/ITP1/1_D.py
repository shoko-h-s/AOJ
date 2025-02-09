# 時計

s = int(input())

# 1時間 = 3600秒
if s >= 3600:
    hour = s // 3600
    
    # msは分・秒に変換する秒数を表す
    ms = s % 3600
else:
    hour = 0
    # 1時間以下となる場合でも、msをsで更新する必要あり
    ms = s
    
if ms >= 60:
    minute = ms // 60
    second = ms % 60
    
else:
    minute = 0
    second = ms
    
print(f"{hour}:{minute}:{second}")
