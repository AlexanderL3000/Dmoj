nums = int(input())
arr = []
out = []
for i in range(nums):
    arr.append(input())

for item in arr:
    count = int(item)
    while True:
        
        if str(count ** 3)[-3:] == "888":
            out.append(count)
            break
        else:
            count += 1

print(*out, sep = "\n")