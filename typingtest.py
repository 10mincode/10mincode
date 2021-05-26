import time
para="yashi"

print("Welcome to Typing Test Adda")
input("Press enter to continue")
print(para)
print()
starttime=time.time()
inputtest=input("Enter the above paragraph\n")
endtime=time.time()
count=0
timetaken=str(endtime-starttime)+"secs"
#i- index
#c-value
for i,c in enumerate(para):
    try:
        if inputtest[i]==c:
            count+=1
    except:
        pass

#x/y*100
accuracy=count/len(para)*100
#5 letters -1 word
wpm=(len(inputtest)*60/(5*(endtime-starttime)))#Words per minute
kps=len(inputtest)/(endtime-starttime)#key per second

print(f'TIme Taken: {timetaken} accuracy: {accuracy}%  {wpm}wpm  {kps}kps')
