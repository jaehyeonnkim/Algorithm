N = int(input())
i = 2

while i <= N:
    if N % i == 0:
        N = N // i
        print(i)
    else:
        i += 1

