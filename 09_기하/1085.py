x, y, w, h = map(int, input().split())

min1 = x if x < w - x else w - x
min2 = y if y < h - y else h - y

print(min1 if min1 < min2 else min2)