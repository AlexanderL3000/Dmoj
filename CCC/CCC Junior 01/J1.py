inp = int(input())
for i in range(1,2*inp,2):
    if i < inp:
        print ('*'*i+" "*((inp*2-2*i))+'*'*(i))
    
    elif i> (inp):
        print ('*' * ((inp*2)-i) + " "*(2*(i-inp)) + "*" * ((inp*2)-i))
    else:
       print ('*' *2*inp)



