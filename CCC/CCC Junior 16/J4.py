hour,min = input().split(":")

start = int(hour) * 60 + int(min)
end = start + 120
slowed_mins = 0
elapsed = 0
if start in range(420, 600): #7-10 
    elapsed = 600-start
    slowed_mins = elapsed/2
elif start == 400:
    elapsed = 180
    slowed_mins = 90


elif end in range(420, 600): #7-10 
    elapsed = (420 - end)
    slowed_mins = elapsed*2

    
elif start in range(900,1140):  #15-19
    elapsed = (1140 - start)
    slowed_mins = elapsed/2
   

elif end in range(900,1140):  #15-19
    elapsed = (900-end)
    slowed_mins = elapsed*2


final = start + elapsed + (120-slowed_mins)
if final >=1440:
    final-=1440
fmin = int(final%60)
fhour = int((final - fmin) / 60)

if(fhour < 10):
    fhour = "0"+str(fhour)
if(fmin < 10):
    fmin = "0"+str(fmin)

print(str(fhour)+":"+str(fmin))