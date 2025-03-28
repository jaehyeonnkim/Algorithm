# 다섯줄의 입력
A = [list(input()) for _ in range(5)]
max_len = max(len(A) for i in A)

# 배열을 세로로 순회
# 0,0, 1,0 2,0 3,0
for i in range(max_len):
    for j in range(max_len):
        print(A[j][i], end='')