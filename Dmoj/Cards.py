inp = int(input())
total = 0

for i in range(inp):
    cards = input()
    for j in range(len(cards)):
        if cards[j] == "A":
            total +=4
        elif cards[j] == "K":
            total +=3
        elif cards[j] == "Q":
            total +=2
        elif cards[j] == "J":
            total +=1
        else:
            pass

print(total)