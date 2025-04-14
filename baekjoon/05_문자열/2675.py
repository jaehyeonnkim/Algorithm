S = int(input())

for _ in range(S):
    A, B = input().split()
    A = int(A)
    result=""
    for i in range(0, len(B)):
        result += B[i]*A

    print(result)