num = int(input())
nums = []

for i in range(num):
    nums.append(int(input()))
    
print(*sorted(nums), sep = "\n")
