side, rad = input().split()


def solve(side,rad):
    sqr = side * side
    circ = 3.14*rad*rad

    if(sqr > circ):
        return True
    else:
        return False

if(solve(int(side), int(rad))):
    print("SQUARE")

else:
    print("CIRCLE")