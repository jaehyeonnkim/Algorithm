N = int(input())

i = 1 # 시작범위
cnt = 1 # 이동수

while N > i:
    i += 6 * cnt
    cnt += 1

print(cnt)