num1 = int(input())
num2 = int(input())
factors = 0
correct = 0

for i in range(num1, num2+1):
    for j in range(1, i+1):
        if(i % j == 0):
            factors +=1
    if factors == 4:
        correct += 1

    factors = 0     

print(f"The number of RSA numbers between {num1} and {num2} is {correct}")    

