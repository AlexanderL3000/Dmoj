inp = input().split()
count = 0
for i in inp:
    if i == "not":
        count += 1
    elif i == "True":
        if(count %2 == 0):
            print("True")
        else:
            print("False")
    else:
        if(count %2 == 0):
            print("False")
        else:
            print("True")