A, B = map(int, input().split())

#A가 B보다 큰 경우에는 '>'를 출력한다.
#A가 B보다 작은 경우에는 '<'를 출력한다.
#A와 B가 같은 경우에는 '=='를 출력한다.
if A > B :
    print(">")
elif A < B :
    print("<")
else :
    print("==")