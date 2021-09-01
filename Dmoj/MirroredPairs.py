print("Ready")
running = True
while running:
    inp = list(input())
    if(inp[0] == inp[1] == " "):
        running = False
        break
    else:
        if(inp[0] =="b" and inp[1] == "d"):
            print("Mirrored pair")
        elif(inp[1] =="b" and inp[0] == "d"):
            print("Mirrored pair")

        elif(inp[0] =="q" and inp[1] == "p"):
            print("Mirrored pair")
        elif(inp[1] =="q" and inp[0] == "p"):
            print("Mirrored pair")
        
        else:
            print("Ordinary pair")