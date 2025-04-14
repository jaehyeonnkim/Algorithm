X = int(input())

line = 1 # 몇 번째 줄
count = 1 # 누적 갯수

# 몇 단계인지 찾기
while X > count:
    line += 1
    count += line
    # line : 5, 
    print("line : " , line ,  "count :", count )

# X가 14라면 5번째 줄 4번째 칸
offset = count - X

 