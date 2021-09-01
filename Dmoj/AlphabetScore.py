word = list(input())
sum = 0
for i in word:
    sum += (ord(i) - 96)


print(sum)