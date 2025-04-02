M = int(input())
N = int(input())

result = []

# 소수 찾기
for i in range(M, N+1):
    if i < 2:
        continue

    is_decimal = True
    
    for idx in range(2, int((i**0.5)+1)):
        if i % idx == 0:
            is_decimal = False
            break
    if is_decimal == True:
        result.append(i)


if len(result) != 0:
    print(sum(result))
    print(min(result))
else:
    print(-1)