count = int(input())
current = 0
names = []
paid = []

for i in range(count):
    names.append(input())
    paid.append(int(input()))
    if paid[i] > paid[current]:
        current = i

print(names[current])
        

    
