A, B, V = map(int,input().split())

day = 0
sum = 0

while sum < V:
    sum += A
    day += 1
    if sum >= V:
        break
    else:
        sum -= B

print(day)    