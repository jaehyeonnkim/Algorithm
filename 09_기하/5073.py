
while True:
    triangle_list = list(map(int, input().split()))

    if sum(triangle_list) == 0:
        break
    if sum(triangle_list) - max(triangle_list) <= max(triangle_list):
        print("Invalid")
    elif len(set(triangle_list)) == 1:
        print("Equilateral")
    elif len(set(triangle_list)) == 2:
        print("Isosceles")
    else:
        print("Scalene")