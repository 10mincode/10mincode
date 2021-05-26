import random
from time import sleep
import keyboard
import cv2
import cvzone

vid=cv2.VideoCapture(0)
detector= cvzone.HandDetector(maxHands=1,detectionCon=0.7)
donepressable=True
nextpressable=False
compmess=""
usermess=""
fixed=[]
fingers=[]
myscore=0
compscore=0
listofchance=[[0, 1, 1, 1, 1], [1, 1, 0, 1, 0], [1, 1, 0, 0, 0], [0, 1, 0, 1, 1], [0, 0, 0, 1, 1], [0, 0, 0, 0, 1], [0, 1, 1, 0, 1], [1, 0, 0, 0, 0], [1, 0, 1, 1, 1], [0, 0, 1, 0, 1], [1, 1, 1, 1, 0], [1, 0, 1, 1, 0], [1, 1, 0, 0, 1], [0, 1, 0, 0, 0], [0, 1, 1, 1, 0], [1, 1, 1, 1, 1], [1, 1, 1, 0, 1], [1, 1, 1, 0, 0], [0, 1, 1, 0, 0], [0, 0, 0, 1, 0], [1, 0, 0, 1, 0], [0, 1, 0, 1, 0], [1, 0, 1, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 1, 1, 0], [0, 1, 0, 0, 1], [1, 0, 1, 0, 0], [1, 0, 0, 0, 1], [0, 0, 1, 1, 1], [1, 0, 0, 1, 1], [1, 1, 0, 1, 1]]
userchances=[]
sumslist={}

for i in listofchance:
    if i.count(1)>1:
        sumslist[str(i)]=i.count(1)
    elif i[0] ==1:
        sumslist[str(i)]=6
    elif i[4] ==1:
        sumslist[str(i)]=4
    else:
        sumslist[str(i)]=1

print(sumslist)
isuserbatting=True
def maxcount(list):
    now=list[0]
    nowcount=list.count(list[0])
    for i in list:
        if list.count(i)>nowcount:
            now=i
    return now
def mincount(list):
    now=list[0]
    nowcount=list.count(list[0])
    for i in list:
        if list.count(i)<nowcount:
            now=i
    return now
whiteframe = cv2.imread("white.png")

compframe = cv2.imread("white.png")

while True:
    success,img=vid.read()
    compframe=whiteframe
    compframe = cv2.resize(compframe, (400, 400))
    img=cv2.flip(img,flipCode=1)
    img=cv2.rectangle(img,(100,50),(550,450),(0, 255, 0),5)
    imgframe=img[50:450,100:550]
    imgframe=cv2.putText(imgframe,f"You: {str(myscore)}",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    imgframe=cv2.putText(imgframe,f"Comp: {str(compscore)}",(200,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    imgframe=cv2.putText(imgframe,usermess,(75,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,255,0),2)
    imgframe=cv2.putText(imgframe,compmess,(75,150),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)
    imgframe=detector.findHands(imgframe)
    lmlist, bbox = detector.findPosition(imgframe)
    compframe=cv2.putText(compframe,f"Computer: ",(20,30),cv2.FONT_HERSHEY_SIMPLEX,1,(0,0,255),2)

    if keyboard.is_pressed('d') and donepressable:
        if lmlist:
            fingers = detector.fingersUp()
            if fingers.count(1)>0:
                donepressable=False

                fixed=fingers
                print(fixed)
    if len(fixed)>0:
        if isuserbatting:
            if len(userchances)>3:
                compchance = maxcount(userchances)
                print(compchance)
            else:
                compchance=random.choice(listofchance)
        else:
            compchance=random.choice(listofchance)
        userchance=fixed
        userchances.append(userchance)
        compframe = cv2.putText(compframe, f"{compchance}", (20, 80), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2)

        if isuserbatting and userchance==compchance:
            isuserbatting=False
            fixed=[]
            nextpressable=True
            print("You Out NOw Bowl Computer")
            compmess="You Out. Now It's Your Bowling"
            print(fixed,compchance)
        elif isuserbatting==False and userchance==compchance:
            isuserbatting=True
            fixed=[]
            nextpressable=True
            print("Computer Out NOw It's your batting")
            usermess="Comp Out. Now It's Your Batting"
            print(fixed,compchance)

        else:
            print("Nothing Done")
            print(fixed,compchance)
            fixed=[]
            nextpressable=True
            if isuserbatting:
                myscore+=sumslist.get(str(userchance))
            else:
                compscore+=sumslist.get(str(compchance))
            print(nextpressable,donepressable,myscore)
    if keyboard.is_pressed('n') and nextpressable:
        donepressable=True
        nextpressable=False
        usermess=""
        compmess=""
        print(nextpressable, donepressable)

    cv2.imshow("Capture",compframe)
    cv2.imshow("CaptureFrame",imgframe)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
vid.release()
# Destroy all the windows
cv2.destroyAllWindows()
