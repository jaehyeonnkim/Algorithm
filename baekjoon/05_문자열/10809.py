S = input()  # 문자열 입력받기

for char in range(97, 123):  # 'a'~'z'의 아스키 코드 범위 (97~122)
    print(S.find(chr(char)), end=" ")