N, B = (input().split())
B = int(B)
result = 0

for i, char in enumerate(reversed(N)):
    if char.isdigit():
        val = ord(char) - ord('0')
    else:
        val = ord(char) - ord('A') + 10
    result += val * B**i    
print(result)
