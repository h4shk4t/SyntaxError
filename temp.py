
import cv2
import time
import mediapipe as mp
import math
cap=cv2.VideoCapture(1)
print("Keep your hands out upright and move them")
mpHands=mp.solutions.hands
hands=mpHands.Hands(False)
mpDraw=mp.solutions.drawing_utils
pTime=0
cTime=0
temp=40
def chords(key="Am"):
    C = ["C","Dm","Em","F","G","Am","Bdim"]
    Cs = ["C#","D#m","Fm","F#","G#","A#m","Cdim"]
    D = ["D","Em","F#m","G","A","Bm","C#dim"]
    Ds = ["D#","Fm","Gm","G#","A#","Cm","Ddim"]
    E = ["E","F#m","G#m","A","B","C#m","D#dim"]
    F = ["F","Gm","Am","A#","C","Dm","Edim"]
    Fs = ["F#","G#m","A#m","B","C#","D#m","Fdim"]
    G = ["G","Am","Bm","C","D","Em","F#dim"]
    Gs = ["G#","A#m","Cm","C#","D#","Fm","Gdim"]
    A = ["A","Bm","C#m","D","E","F#m","G#dim"]
    As = ["A#","Cm","Dm","D#","F","Gm","Adim"]
    B = ["B","C#m","D#m","E","F#","G#m","A#dim"]
    if key.lower() in ("c","am"):
        return C
    elif key.lower()in ("c#","a#m"):
        return Cs
    elif key.lower() in ("d","bm"):
        return D
    elif key.lower() in ("d#","cm"):
        return Ds
    elif key.lower() in ("e","c#m"):
        return E
    elif key.lower() in ("f","dm"):
        return F
    elif key.lower() in ("f#","d#m"):
        return Fs
    elif key.lower() in ("g","em"):
        return G
    elif key.lower() in ("g#","fm"):
        return Gs
    elif key.lower() in ("a","f#m"):
        return A
    elif key.lower() in ("a#","gm"):
        return As
    elif key.lower() in ("b","g#m"):
        return B
    
def chord(scale,indR,midR,ringR,pinkR):
    if (indR == 2 and midR == 2 and ringR ==2 and pinkR == 2):
        return "Mute"
    elif ("G" in scale and indR == 1 and midR == 2 and ringR == 0 and pinkR == 0):
        return "G"
    elif ("A" in scale and indR == 1 and midR == 1 and ringR == 0 and pinkR == 0):
        return "A"
    elif ("C" in scale and indR == 0 and midR == 0 and ringR == 2):
        return "C"
    elif ("E" in scale and midR==2 and ringR == 2 and indR==1):
        return "E"
    #D chord me vansh help kardiyooo Im not sure ki yeh sahi combination hai
    elif ("D" in scale and indR == 0 and midR == 0 and ringR == 0 and pinkR == 0):
        return "D"
    elif ("Am" in scale and midR == 1 and ringR == 1 and indR == 0 and pinkR == 0):
        return "Am"
    elif ("Em" in scale and (((indR == 2 and midR == 2 and ring ==0) or (midR==2 and ringR == 2 and indR == 0))) and pinkR == 0):
        return "Em"
    elif ("Dm" in scale and indR == 0 and midR == 1 and ringR == 0 and pinkR == 0):
        return "Dm"
    elif ("F" in scale and indR == 2 and midR == 1 and ringR == 2 and pinkR == 2):
        return "F"
    #elif ("Fm" in scale and indR == 2 and ringR == 2 and pinkR == 2):
    #    return "Fm"
    else:
        print("Bhai guitar bajana seekhle")
        return ""

def play(chord,strum):
    if (chord == "G" and strum == "Up"):
        #play the chord
        pass

while temp>=0:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    print(results.multi_hand_landmarks)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    if results.multi_hand_landmarks:
        temp-=1
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
                    mid=math.hypot(x12-x0,y12-y0)
                    ring=math.hypot(x16-x0,y16-y0)
                    pink=math.hypot(x20-x0,y20-y0)
                    palm=math.hypot(x5-x0,y5-y0)
                    print(palm/ind)
while True:
    success,img=cap.read()
    imgRGB=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    results=hands.process(imgRGB)
    iN = 0
    mN = 0
    rN = 0
    pN = 0
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
            x4=xList[4]
            if x4>x8:
                print("Left")
            else:
                print("Right")
            #index inger
            ''' print(math.hypot(x8-x0,y8-y0)/math.hypot(x5-x0,y5-y0))
            print("Index Finger is: ")
            if math.hypot(x8-x0,y8-y0)/math.hypot(x5-x0,y5-y0)>(round(ind/palm,1)-0.1):
                print("Raised")
                iN=2
            elif (math.hypot(x8-x0,y8-y0)/math.hypot(x5-x0,y5-y0))>(3*(round(ind/palm,1))/4):
                print("Half")
                iN=1
            else:
                print("Down")
                iN=0
            #middle finger
            print(math.hypot(x8-x0,y8-y0)/math.hypot(x5-x0,y5-y0))
            print("Middle Finger is: ")
            if math.hypot(x12-x0,y12-y0)/math.hypot(x5-x0,y5-y0)>(round(mid/palm,1)-0.1):
                print("Raised")
                mN=2
            elif (math.hypot(x12-x0,y12-y0)/math.hypot(x5-x0,y5-y0))>(3*(round(mid/palm,1))/4):
                print("Half")
                mN=1
            else:
                print("Down")
                mN=0
            #ring finger
            print(math.hypot(x16-x0,y16-y0)/math.hypot(x5-x0,y5-y0))
            print("Ring Finger is: ")
            if math.hypot(x16-x0,y16-y0)/math.hypot(x5-x0,y5-y0)>(round(ring/palm,1)-0.02):
                print("Raised")
                rN=2
            elif (math.hypot(x16-x0,y16-y0)/math.hypot(x5-x0,y5-y0))>(3*(round(ring/palm,1))/4):
                print("Half")
                rN=1
            else:
                print("Down")
                rN=0
            #pinky finger
            print(math.hypot(x20-x0,y20-y0)/math.hypot(x5-x0,y5-y0))
            print("Pinky Finger is: ")
            if math.hypot(x20-x0,y20-y0)/math.hypot(x5-x0,y5-y0)>(round(pink/palm,1)-0.02):
                print("Raised")
                pN=2
            elif (math.hypot(x20-x0,y20-y0)/math.hypot(x5-x0,y5-y0))>(3*(round(pink/palm,1))/4):
                print("Half")
                pN=1
            else:
                print("Down")
                pN=0
            print(chord(chords(),iN,mN,rN,pN))'''
        mpDraw.draw_landmarks(img,i,mpHands.HAND_CONNECTIONS)
    cTime=time.time()
    fps=1/(cTime-pTime)
    pTime=cTime
    cv2.putText(img,str(int(fps)),(10,70),cv2.FONT_HERSHEY_PLAIN,3,(255,0,255),3)
    cv2.imshow("Image",img)
    cv2.waitKey(1)
    
