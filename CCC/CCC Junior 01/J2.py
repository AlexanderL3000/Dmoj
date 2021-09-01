inp1 = int(input())
inp2 = int(input())

working = False
for i in range(inp2):
    if (inp1 * i) % inp2 == 1:
        print (i)
        working = True
    
if not working:
    print("No such integer exists.")
    