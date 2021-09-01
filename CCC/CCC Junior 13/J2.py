inp = input()

for letter in inp:
    if(letter not in list('IOSHZXN')):
        print("NO")
        break
else:
    print("YES")