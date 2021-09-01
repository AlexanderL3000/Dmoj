pw = input()

letters = len(pw)
lower = 0
upper = 0
digit = 0


for letter in list(pw):
    if(letter.islower()):
        lower += 1
    elif(letter.isupper()):
        upper += 1
    elif(letter.isdigit()):
        digit += 1


if(letters in range(8,13) and lower >= 3 and upper >=2 and digit>=1):
    print("Valid")
else:
    print("Invalid")