import cv2
import mediapipe as mp
import time
import math
cap=cv2.VideoCapture(0)
mpHands=mp.solutions.hands
hands=mpHands.Hands(False)
mpDraw=mp.solutions.drawing_utils
pTime=0
cTime=0
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
            x1=xList[5]
            y1=yList[5]
            x2=xList[0]
            y2=yList[0]
            x4=xList[8]
            y4=yList[8]
            x1=x4-x2
            y1=y4-y2
            x2=x2-x1
            y2=y2-y1
            if math.hypot(x1,y1)/math.hypot(x2,y2)>0.2:
                print("YES")
            else:
                print("No")
            mpDraw.draw_landmarks(img,i,mpHands.HAND_CONNECTIONS)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
                
