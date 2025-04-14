N = int(input())
nums = list(map(int, input().split()))
count = 0

for num in nums:
    if num < 2:
        continue
    is_decimal = True

    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_decimal = False
            break
    if is_decimal:
        count += 1

print(count)

