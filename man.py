from cv2 import *
import numpy
from PIL import ImageTk, Image
from time import sleep
#load the trained model to classify sign
from keras.models import load_model
model = load_model('50my_model.h5')


#dictionary to label all traffic signs class.
classes = { 1:'Speed limit (50km/hr)',2:'No sign'}

#cascade=CascadeClassifier("cross.xml")
cam=VideoCapture(0)
#cam.set(3,320)
#cam.set(4,240)
i=0

while True:
    ret,frame=cam.read()
    if ret==True:
        gray=cvtColor(frame,COLOR_BGR2GRAY)
        #detect=cascade.detectMultiScale(gray,scaleFactor=1.1,minNeighbors=5,minSize=(30,30))
        #print(detect)
        imshow('Video',frame)
        #try:
         #   if detect.sizes:
          #      print("Detected")
        #except:
         #   print("No Detect")
          #  pass
        i=i+1
        imwrite('jpg.jpg',frame)
    image = Image.open('jpg.jpg')
    image = image.resize((30,30))
    image = numpy.expand_dims(image, axis=0)
    image = numpy.array(image)
    print(image.shape)
    pred = model.predict_classes([image])[0]
    sign=classes[int(pred)+1]
    print(sign)
    if waitKey(1) and 0xFF==ord('q'):
        break
    
cam.release()
            
