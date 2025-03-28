S = input()
time = 0
for char in S:
    if(char=='A' or char=='B'or char=='C'):
        time += 2
    elif(char=='D'or char=='E'or char=='F'):    
        time += 3
    elif(char=='G'or char=='H'or char=='I'):    
        time += 4
    elif(char=='J'or char=='K'or char=='L'):    
        time += 5
    elif(char=='M'or char=='N'or char=='O'):    
        time += 6
    elif(char=='P'or char=='Q'or char=='R'or char=='S'):    
        time += 7
    elif(char=='T'or char=='U'or char=='V'):    
        time += 8
    elif(char=='W'or char=='X'or char=='Y'or char=='Z'):
        time += 9

    
time += len(S)
print(time)