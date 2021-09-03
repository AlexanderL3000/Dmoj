count = int(input())

aCount = 100
bCount = 100

for i in range(count):
    a,b = input().split(" ")
    a,b = int(a), int(b)

    if a < b:
        aCount -= b
    elif a>b:
        bCount -= a

print(aCount)
print(bCount)