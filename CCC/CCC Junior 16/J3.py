inp = input()
max = 1
for i in range(len(inp)):
    count = 0
    for j in range(i, len(inp)+1):
        backwards = ''
        for letter in inp[i:j]:
            backwards = letter+backwards
        if inp[i:j] == backwards:
            counter = len(inp[i:j])
        if max<counter:
            max = counter
        
print(max)