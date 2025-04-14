A = int(input())

if A >= 90 and A <=100:
    print("A")
elif A >= 80 and A <=89:
    print("B")
elif A >= 70 and A <= 79:
    print("C")
elif A >=60 and A <= 69:
    print("D")
else:
    print("F")


# 더 효율적
A = int(input())

if A >= 90:
    print("A")
elif A >= 80:
    print("B")
elif A >= 70:
    print("C")
elif A >= 60:
    print("D")
else:
    print("F")
