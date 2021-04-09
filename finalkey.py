import sys
import cv2
cascade=cv2.CascadeClassifier("cross.xml")
cam=cv2.VideoCapture(0)
#cam.set(3,320)
#cam.set(4,240)
i=0
while True:
    ret,frame=cam.read()
    if ret==True:
        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        detect=cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
        print(detect)
        try:
            print(detect.sizes)
            if detect.sizes:
                print("Detected")
        except:
            print("No Detect")
        for (x,y,w,h) in detect:
            cv2.rectange(frame,(x,y),(x+w,y+h),(0,255,0),2)
        cv2.imshow('Video',frame)
        i=i+1
    if cv2.waitKey(1) and 0xFF==ord('q'):
        break
cam.release()
            
