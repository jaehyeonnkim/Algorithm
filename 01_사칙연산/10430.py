# A, B, C 순서대로 입력됨
A, B, C = map(int, input().split())

# 첫째줄에  (A+B)%C, 
# 둘째 줄에 ((A%C) + (B%C))%C, 
# 셋째 줄에 (A×B)%C, 
# 넷째 줄에 ((A%C) × (B%C))%C를 출력
print((A+B)%C)
print(((A%C) + (B%C))%C)
print((A*B)%C)
print(((A%C) * (B%C))%C)