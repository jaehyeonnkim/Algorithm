a, b = map(int, input().split())
c, d = map(int, input().split())
e, f = map(int, input().split())

x = a if a != c and a != e else c if a == e else e
y = b if b != d and b != f else d if b == f else f

print(x, y)