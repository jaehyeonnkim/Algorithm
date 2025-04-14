A = set(range(1, 5))

for _ in range(3):
    A.remove(int(input()))

print(*sorted(A))