message = input().split()
count = int(input())

for i in range(count):
    inp = input()
    new = message[:]
 
    for word in range(len(new)):
        new[word] = new[word].replace(">", inp)
        
    new = " ".join(new)
    print(new)

