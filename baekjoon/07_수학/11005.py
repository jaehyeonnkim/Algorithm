N, B = (map(int,input().split()))
result = []

# 35 
while N > 0:
    val = N % B

    if val < 10:
        result.append(str(val))
    else:
        result.append(chr(ord('A') + val - 10))

    N = N // B

print(''.join(reversed(result)))