A = int(input())
B = int(input())

#1의 자리
B1 = B % 10

#10의 자리
B10 = (B // 10) % 10

#100의 자리
B100 = B//100


print(A * B1)
print(A * B10)
print(A * B100)
print(A * B)