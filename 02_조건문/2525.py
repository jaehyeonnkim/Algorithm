A, B = map(int, input().split())
C = int(input())

if B + C >= 60 :
    A = A + (B+C)//60
    if A >= 24 :
        print(A-24, (B+C)%60)
    else :
        print(A, (B+C)%60 )
else:
    print(A, B + C)

#피리 답
A, B = map(int, input().split())
C = int(input())

# 총 분 계산
total_minutes = A * 60 + B + C

# 새로운 시, 분 계산
A = (total_minutes // 60) % 24  # 24시간을 넘어가면 % 24로 조정
B = total_minutes % 60

print(A, B)
