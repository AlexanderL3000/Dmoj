rounds = int(input())
svenhand = list(input())
total = 0
friends = int(input())


for i in range(friends):
    other = list(input())
    for j in range(len(svenhand)):
        if(svenhand[j] == other[j]):
            total += 1
        elif(svenhand[j] == "S" and other[j] == "P" ):
            total += 2
        elif(svenhand[j] == "P" and other[j] == "R" ):
            total += 2
        elif(svenhand[j] == "R" and other[j] == "S" ):
            total += 2
        else:
            pass
    
print(total)
