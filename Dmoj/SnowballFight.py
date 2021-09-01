h1, w1 = input().split()
h2, w2 = input().split()

h1,w1,h2,w2 = int(h1),int(w1),int(h2),int(w2)

if(w1 * (h2-1) > w2 * (h1-1)):
    print(2)
elif(w1 * (h2-1) < w2 * (h1-1)):
    print(1)
else:
    print(-1)