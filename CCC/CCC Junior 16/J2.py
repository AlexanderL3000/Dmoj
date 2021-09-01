nums = []
s = 0
total = 0
rowsum = 0

for i in range (4):
    nums.append(input().split())
    
    for num in nums[i]:
        s += int(num)
    
   
for i in range(4):
    for j in range(4):
        s += int(nums[j][i])
    
for num in nums[i]:
    rowsum += int(num)
if(s/8 == rowsum):
    print("magic")
else:
    print("not magic")  

