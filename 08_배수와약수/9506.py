result = []
total = 0
char_list = []

while True:
    n = int(input())
    if n == -1:
        break

    result = []
    total = 0
    char_list = []

    for i in range(1, n):
        if n % i == 0:
            result.append(i)  
    for val in result:
        total += val
        char_list.append(str(val))
    if total == n:
        final_str = ' + '.join(char_list)
        print(f"{n} = {final_str}")
    else:
        print(f"{n} is NOT perfect.")