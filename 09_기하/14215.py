triangle_list = list(map(int, input().split()))
max = max(triangle_list)
mod = sum(triangle_list) - max
if max >= mod:
    max = mod - 1
 
print(max + mod)