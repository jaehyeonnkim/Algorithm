A, B, C = map(int, input().split())

if A == B == C :
    print(10000 + (A*1000))
elif A == B and B != C and A != C:
    print(1000 + (A*100))
elif A != B and B == C and A != C:
    print(1000 + (B*100))
elif A != B and B != C and A == C:
    print(1000 + (C*100))
else:
    if A > B: #A가 클 때 
        if A < C : #C가 제일 클 때
            print(C*100)
        if A > C : 
            print(A*100)
    elif A < B : # B가 클 때
        if B < C :
            print(C*100)
        if B > C :
            print(B*100)

# 피리 버전
if A == B == C:
    print(10000 + (A * 1000))

elif A == B or A == C:
    print(1000 + (A * 100))
elif B == C:
    print(1000 + (B * 100))

else:
    print(max(A, B, C) * 100)