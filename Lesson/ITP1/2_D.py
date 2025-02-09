# 長方形の中の円

w, h, x, y, r = map(int, input().split())

if (x + r <= w) and (y + r <= h) and (x - r >= 0) and (y - r >= 0):
    print("Yes")
else:
    print("No")
