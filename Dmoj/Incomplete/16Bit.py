lines = int(input())

for i in range(lines):
    a,b,p = input().split(" ")
    if int(a) * int(b) == int(p):
        print("POSSIBLE DOUBLE SIGMA")
    else:
        print("16 BIT S/W ONLY")