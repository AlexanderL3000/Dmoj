from collections import Counter

count = int(input())
arr = []
swaps = True
lst = ["Deluxe Tuna Bitz", "Bonito Bitz", "Sashimi", "Ritzy Bitz"]

for i in range(count):
    arr.append(input())

cnt = Counter(arr)
cnt=cnt.most_common()
while swaps != False:
    for i, items in enumerate(cnt):
        if i+1 < len(cnt):
        
            if(items[1]==cnt[i+1][1]):
                if(lst.index(items[0])>lst.index(cnt[i+1][0])):
                    cnt[i], cnt[i+1] = cnt[i+1], cnt[i]
                    break
    else:
        swaps = False


for items in cnt:
    print(str(items[0]) + " "+ str(items[1]))
