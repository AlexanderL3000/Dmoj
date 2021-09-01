time = int(input())
num = int(input())
count = 0

mins = []
for i in range(num):
    mins.append(int(input()))

mins = sorted(mins)

for item in mins:
    if (time - item >= 0):
        time -= item
        count += 1

print(count) 