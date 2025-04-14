# 10x10 배열만들기
A = [[0]* 100 for _ in range(100)]

n = int(input())

# 입력받기
for _ in range(n):
    x, y = map(int, input().split())

# 채워진부분 1로 채우기
    for i in range(x, x+10):
        for j in range(y, y+10):
            A[i][j] = 1

area = 0
for i in A:
    area += sum(i)

print(area)

