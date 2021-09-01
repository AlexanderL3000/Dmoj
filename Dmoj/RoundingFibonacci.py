nums = 5

def check(min, max, val):
    if val-min< max-val:
        return min
    elif val-min > max-val:
        return max
    else:
        return max


for _ in range (nums):
    a, b = 0, 1
    inp = int(input())
    while(True):
        a, b = b, a+b

        if(b > inp):
            print(check(a,b, inp))
            break
        elif(b == inp):
            print(inp)
            break
       





        
        
