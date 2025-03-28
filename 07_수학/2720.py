T = int(input())

for _ in range(T):
    C = int(input())
    a = C // 25     # a는 124//25 = 4
    b = (C % 25) // 10    # b는 124%25=24에서 24//10 = 2
    c = ((C % 25) % 10) // 5     # c는 24%10=4에서 4//5 = 0
    d = ((C % 25) % 10 % 5) // 1
    print(a, b, c, d)

# 피티헴
T = int(input())
coins = [25, 10, 5, 1]

for _ in range(T):
    C = int(input())
    result = []
    for coin in coins:
        result.append(C // coin)
        C %= coin