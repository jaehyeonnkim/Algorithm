# N = int(input())

# list = list(map(int, input().split()))

# print(min(list), max(list))

N = int(input())

list = list(map(int, input().split()))
min = list[0]
max = list[0]

for i in list:
    if i < min:
        min = i 
    if i > max:
        max = i

print(min, max)