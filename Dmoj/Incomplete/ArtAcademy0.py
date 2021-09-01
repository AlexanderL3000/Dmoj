inp = int(input())

for i in range(inp):
    name = input()
    for j in name:
        if j == 'A'.lower():
            print("Hi!", end = " ")
        elif j == 'E'.lower():
            print("Bye!",end = " ")
        elif j == 'I'.lower():
            print("How are you?",end = " ")
        elif j == 'O'.lower():
            print("Follow me!",end = " ")
        elif j == 'U'.lower():
            print("Help!", end = " ")
        elif j.isdigit():
            print("Yes!",end = " ")
        else:
            pass
    print()
    