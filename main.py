import cv2
from cvzone import HandTrackingModule as htm
img1=cv2.imread("infinity.jpg")
img1 = cv2.resize(img1,(100,100))
imgH,imgW,_=img1.shape
tempH,tempW=100,100
#print(imgH,imgW)
cap=cv2.VideoCapture(0)
cap.set(3,1000)
cap.set(4,1000)
hand_detector=htm.HandDetector()
while True:
    _,img=cap.read()
    #print(img.shape)
    hand_no,img=hand_detector.findHands(img)
    img[tempH:tempH+int(imgH),tempW:tempW+int(imgW)]=img1
    if hand_no:
        hand1=hand_no[0]
        #print(hand1)
        fingure_list=hand_detector.fingersUp(hand1)
        x1,y1=hand1['lmList'][8]
        #x2,y2=hand1['lmList'][12]
        cv2.circle(img,(x1,y1),5,(0,255,0),cv2.FILLED)
        if fingure_list==[0,1,1,0,0] and tempH<y1<(tempH+imgH) and tempW<x1<(tempW+imgW):
            tempH=y1-imgH//2
            tempW=x1-imgW//2
        try:
            img[tempH:tempH+imgH,tempW:tempW+imgW]=img1
        except:
            pass
        #print(fingure_list)
    cv2.imshow("main image",img)
    #cv2.imshow("drag image",img1)
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break