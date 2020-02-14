import cv2
import numpy as np
import subprocess
import time
import datetime
recognizer = cv2.face.LBPHFaceRecognizer_create()
recognizer.read('trainner-new/trainner.yml')
cascadePath = "haarcascade_frontalface_default.xml"
faceCascade = cv2.CascadeClassifier(cascadePath);


cam = cv2.VideoCapture(0)
font = cv2.FONT_HERSHEY_SIMPLEX
unknown_cnt=0
Id=0
#font = cv2.cv.InitFont(cv2.cv.CV_FONT_HERSHEY_SIMPLEX, 1, 1, 0, 1, 1)
while True:
    ret, im =cam.read()
    gray=cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
    faces=faceCascade.detectMultiScale(gray, 1.2,5)
    for(x,y,w,h) in faces:
        cv2.rectangle(im,(x,y),(x+w,y+h),(225,0,0),2)
        Id, conf = recognizer.predict(gray[y:y+h,x:x+w])
        print(Id,"--",conf)
        if(conf<50):
            if(Id==5):
                Id="Family Member"
            elif(Id==2):
                Id="Family Member"
            #else:
             #   Id="Unknown"
                
                
        else:
            Id="Intruder"
            #print("Intruder")
        #cv2.cv.PutText(cv2.cv.fromarray(im),str(Id), (x,y+h),font, 255)
        #cv2.PutText(im,str(Id), (x,y+h),font, 255)
        cv2.putText(im, str(Id), (x,y-40), font, 2, (255, 255, 255), 3)
    cv2.imshow('image',im)
    if(Id=="Intruder"):
        unknown_cnt+=1
        if(unknown_cnt>=100):
            # save screenshot at a given timestamp
            #file_name=str(datetime.datetime.now()).replace(" ","_")+".jpg"
            #file_path="/home/pi/screenshots/intruder_at_"+file_name
            #cv2.imwrite(file_path, gray[y:y+h,x:x+w])
            #time.sleep(30)
            #bashCommand = "python3 send-email.py"
            bashCommand = "python3 fire.py "
            output = subprocess.check_output(['bash','-c', bashCommand])
            time.sleep(30)
            unknown_cnt=0
        
    if cv2.waitKey(10) & 0xFF==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()