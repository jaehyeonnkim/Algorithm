triangle_list = []

for _ in range(3):
    triangle_list.append(int(input()))    

sum = sum(triangle_list)

if sum == 180:
    if len(set(triangle_list)) == 1:
        print("Equilateral")
    elif len(set(triangle_list)) == 2:
        print("Isosceles")
    else: 
        print("Scalene")
else:
    print("Error")