import cv2
import time
import mediapipe as mp
import math
cap=cv2.VideoCapture(0)
print("Keep your hands out upright and move them")
mpHands=mp.solutions.hands
hands=mpHands.Hands(False)
mpDraw=mp.solutions.drawing_utils
pTime=0
cTime=0
for j in range(40):
        success,img=cap.read()
        imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        results=hands.process(imgRGB)
        lx8=[]
        lx0=[]
        lx5=[]
        ly8=[]
        ly5=[]
        ly0=[]
        lx12=[]
        lx16=[]
        lx20=[]
        ly12=[]
        ly16=[]
        ly20=[]
        if results.multi_hand_landmarks:
                xList=[]
                yList=[]
                for i in results.multi_hand_landmarks:
                    for id,lm in enumerate(i.landmark):
                        h, w, c = img.shape
                        cx, cy = int(lm.x * w), int(lm.y * h)
                        xList.append(cx)
                        yList.append(cy)
                    lx8.append(xList[8])
                    lx0.append(xList[0])
                    lx5.append(xList[5])
                    lx12.append(xList[12])
                    lx16.append(xList[16])
                    ly12.append(yList[12])
                    ly16.append(yList[16])
                    lx20.append(xList[20])
                    ly20.append(yList[20])
                    ly8.append(yList[8])
                    ly0.append(yList[0])
                    ly5.append(yList[5])
                    #list
                    x8=(sum(lx8))/40
                    x0=(sum(lx0))/40
                    x5=(sum(lx5))/40
                    x12=(sum(lx12))/40
                    x16=(sum(lx16))/40
                    x20=(sum(lx20))/40
                    y8=(sum(ly8))/40
                    y0=(sum(ly0))/40
                    y5=(sum(ly5))/40
                    y12=(sum(ly12))/40
                    y16=(sum(ly16))/40
                    y20=(sum(ly20))/40
                    ind=math.hypot(x8-x0,y8-y0)
                    mid=math.hypot(x12-x0,y8-y0)
                    ring=math.hypot(x16-x0,y16-y0)
                    pink=math.hypot(x20-x0,y20-y0)
                    palm=math.hypot(x5-x0,y5-y0)
                    print(palm/ind)
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    if results.multi_hand_landmarks:
        xList=[]
        yList=[]
        for i in results.multi_hand_landmarks:
            for id,lm in enumerate(i.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x * w), int(lm.y * h)
                xList.append(cx)
                yList.append(cy)
            x0=xList[0]
            y0=yList[0]
            x5=xList[5]
            y5=yList[5]
            x8=xList[8]
            y8=yList[8]
            x12=xList[12]
            y12=yList[12]
            x16=xList[16]
            y16=yList[16]
            x20=xList[20]
            y20=yList[20]
            #index finger
            print(math.hypot(x8-x0,y8-y0)/math.hypot(x5-x0,y5-y0))
            print("Index Finger is: ")
            if math.hypot(x8-x0,y8-y0)/math.hypot(x5-x0,y5-y0)>(round(ind/palm,1)-0.1):
                print("Raised")
            elif (math.hypot(x8-x0,y8-y0)/math.hypot(x5-x0,y5-y0))>(3*(round(ind/palm,1))/4):
                print("Half")
            else:
                print("Down")
            mpDraw.draw_landmarks(img,i,mpHands.HAND_CONNECTIONS)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    
