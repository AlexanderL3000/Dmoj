run = True
while(run):

    word = input()
    if(word == "quit!"):
        run = False
        break
    else:
        if(word[-1] == 'r' and word[-2] == "o"):
            if(word[-3] not in ('a','e','i','o','u','y') and len(word) > 4):
                word = word.replace("or", "our")
            
        print(word)
