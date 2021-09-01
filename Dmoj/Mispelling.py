inps = int(input())

for i in range (inps):
    letter, word = input().split(" ", 1)
    word = list(word)
    
    word[int(letter)-1] = ""
    print(str(i+1)+" ", end = "".join(word)+"\n")