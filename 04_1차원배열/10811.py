N, M = map(int, input().split())
num = [i for i in range(1, N+1) ]

for _ in range(M):
    i, j = map(int, input().split())
    num[i-1:j] = reversed(num[i-1:j])

print(*num)
