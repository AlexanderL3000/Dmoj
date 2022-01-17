inp = list(input())
pu = list("pusheen")
count = 0

for i in range(len(inp)):
    if inp[i] != pu[i]:
    
        count += 1

print(count)