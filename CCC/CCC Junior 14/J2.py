count = int(input())
letters = input()
aCount = 0
bCount = 0

for letter in letters:
    if letter == 'A':
        aCount+=1
    else:
        bCount+=1

if bCount == aCount:
    print("Tie")

elif bCount < aCount:
    print('A')
else:
    print('B')