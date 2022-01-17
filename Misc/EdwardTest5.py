import math

val = int(input())
arr=[]
new=[]
count = 0
for i in range(1,val**2+1):
    arr.append(i)

for i in range(val):
    inp = input().split()
    for j in inp:
        new.append(j)

for i in range(len(arr)):
    if int(new[i]) != int(arr[i]):
        count += 1
print(math.ceil(math.sqrt(count)))