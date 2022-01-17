count = int(input())

for i in range(count):
    bool = False
    inp = input().split()
    top = int(inp[2])
   
    one = int(inp[0])
    two = int(inp[1])
    bool = False
   
    for i in range(round(top/one)):
        if ((top-one*i) % two == 0) or ((top-one*i) % one == 0):
            bool = True
        else:
            pass
    if bool:
        print("YES")
    else:
        print("NO")
    
    