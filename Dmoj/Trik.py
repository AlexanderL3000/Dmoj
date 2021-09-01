inp = input()
cups = ["ball", "not", "not"]

for i in range(len(inp)):
    if inp[i] == "A":
        cups[0], cups[1] = cups[1], cups[0] 
    elif inp[i] == "B":
        cups[1], cups[2] = cups[2], cups[1] 
    else:
        cups[0], cups[2] = cups[2], cups[0] 


if cups.index("ball") == 0:
    print(1)
elif cups.index("ball") == 1:
    print(2)
else:
    print(3)