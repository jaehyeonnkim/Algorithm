H, M = map(int, input().split())

if M < 45 :
    if H == 0:
        H = H + 23
    else:
        H = H-1 
    M = M + 60 - 45
    print(H, M)
else :
    print(H, M-45)

# 피리 작업
H, M = map(int, input().split())


if M >= 45:
    print(H, M - 45)  # 분만 감소 (시 변화 없음)
else:
    if H == 0:
        print(23, M + 15)  # 0시에서 한 시간 감소하면 23시
    else:
        print(H - 1, M + 15)  # 한 시간 감소, 분은 60분 기준 보정
