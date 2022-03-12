import cv2
import time
import mediapipe as mp
temp=0
cap=cv2.VideoCapture(1)
mpHands=mp.solutions.hands
hands=mpHands.Hands(False)
mpDraw=mp.solutions.drawing_utils
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
            if temp==0:
                temp=1
                x0=xList[8]
                y0=yList[8]
            elif temp==1:
                temp=0
                x1=xList[8]
                y1=yList[8]
                if y1>y0+20:
                    print("Down")
                    time.sleep(0.5)
                elif y0>y1+20:
                    print("UP")
                    time.sleep(0.5)
            mpDraw.draw_landmarks(img,i,mpHands.HAND_CONNECTIONS)
    cv2.imshow("Image",img)
    cv2.waitKey(1)