repeats = int(input())
out = []
for i in range(repeats):
    curr = []
    branch = []
    count = 1
    result = "Y"
    nums = int(input())

    for j in range(nums):
        curr.append(int(input()))
    
    while len(curr) > 0 or len(branch) > 0:
        if len(curr) > 0 and len(branch) > 0:
            if branch[-1] == count:
                branch.pop()
                count += 1
            elif curr[-1] == count:
                curr.pop()
                count += 1
            else: 
                branch.append(curr[-1])
                curr.pop()
        elif len(branch) > 0: 
            if branch[-1] == count:
                branch.pop()
                count += 1
            else: 
                result = "N"
                break
        else:
            if curr[-1] == count:
                curr.pop()
                count += 1
            else:
                branch.append(curr[-1])
                curr.pop()



    if result == "Y":
        out.append("Y")
    else:
        out.append("N")


print(*out, sep = "\n")
