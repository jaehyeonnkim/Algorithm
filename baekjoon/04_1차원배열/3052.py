list = set()

for _ in range(10):
    num = int(input())
    list.add(num%42)

print(len(list))