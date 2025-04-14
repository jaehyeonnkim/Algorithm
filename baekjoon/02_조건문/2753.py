year = int(input())

if year % 4 == 0 and year % 100 != 0:
    print("1")
elif year % 4 == 0 and year % 400 == 0:
    print("1")
else:
    print("0")


# 더 효율적인 것

Y = int(input())

# 윤년 판별
if (Y % 4 == 0 and Y % 100 != 0) or (Y % 400 == 0):
    print(1)  # 윤년
else:
    print(0)  # 평년
