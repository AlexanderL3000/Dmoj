pieces = int(input())
heights = input().split()
widths = input().split()

sum = 0

for i in range(len(widths)):
    sum += int(widths[i]) * (int(heights[i]) + int(heights[i+1]))/2

if sum.is_integer():
    print(int(sum))
else:
    print(sum)