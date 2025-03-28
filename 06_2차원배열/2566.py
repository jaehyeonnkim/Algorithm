A = [list(map(int, input().split())) for _ in range(9)]
max_value = -1
position = [0,0]
for i in range(9):
    for j in range(9):
        if max_value <A[i][j]:
            max_value = A[i][j]
            position = [i+1,j+1]
print(max_value)
print(*position)