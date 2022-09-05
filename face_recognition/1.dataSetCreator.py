import cv2
import numpy as np

facedetect = cv2.CascadeClassifier('haarcascade_frontalface_default.xml');

cam = cv2.VideoCapture(0);  # 0 opens inbuilt camera. time.sleep() will add time delay

id = input('Enter Roll no.')  # id will take a name/number as a ID
NumofImgs = 0

while (1):

    ret, img = cam.read()  # returns a variable and the captured image
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)  # converting coloured image to grayscale
    faces = facedetect.detectMultiScale(gray, 1.3,5)  # method to search for face rectangular coordinates. 1.3 is the scale factor. Decreases the shape value by 5%

    for (x, y, w, h) in faces:
        NumofImgs += 1
        cv2.imwrite("dataSet/User." + str(id) + "." + str(NumofImgs) + ".jpg",
                    gray[y:y + h, x:x + w])  # saves the image in a folder "dataSet"
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 3)  # rectangle to show face
        cv2.waitKey(100)  # waits for 100 milliseconds

    cv2.imshow("Face", img)  # to show output img
    cv2.waitKey(1)

    if (NumofImgs > 20):
        break

cam.release()
cv2.destroyAllWindows()
