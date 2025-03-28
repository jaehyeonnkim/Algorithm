X = int(input())
N = int(input())
sum = 0

for _ in range(N):
    A, B = map(int, input().split())
    sum += A * B

if sum == X:
    print("Yes")
else:
    print("No")