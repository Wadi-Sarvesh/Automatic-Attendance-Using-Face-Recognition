import cv2

from xlrd import open_workbook
from xlutils.copy import copy
import datetime


rd=open_workbook("Template.xls")
wb=copy(rd)

s=wb.get_sheet(0)

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');
cam=cv2.VideoCapture(0);
rec=cv2.face.LBPHFaceRecognizer_create();
rec.read("trainingData.yml")
id=0
font=cv2.FONT_HERSHEY_SIMPLEX

i=str(datetime.date.today())
print(i);
ab=i[8:10:1]
print(ab);


while(1):
    boolval,img=cam.read();                                                  #returns a variable and the captured image
    gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)                            #converting coloured image to grayscale
    faces=facedetect.detectMultiScale(gray,1.3,5);                       #list to store faces
    for (x,y,w,h) in faces:
        cv2.rectangle(img,(x,y),(x+w,y+h),(0,255,0), 2)                  #rectangle to show face
        id,conf=rec.predict(gray[y:y+h,x:x+w])

        for j in range(20):
            if id==j:
                s.write(j,int(ab)+1,int(1))
                wb.save("Output_attendance.xls")

        cv2.putText(img, str(id), (x,y+h),font,1,255);

    cv2.imshow("Face",img);

    if(cv2.waitKey(1)==ord('e')):
        break;
cam.release()
cv2.destroyAllWindows()

