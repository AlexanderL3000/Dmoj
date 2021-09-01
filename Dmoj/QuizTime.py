out = ["b","b","b","b","b"]


for i in range(5):
    curr = input()
    num = (int(input()))
    out[num-1] = curr

print(*out, sep = '\n')
