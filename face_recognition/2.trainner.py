import os                                                                              #for comparing the stored images and train the recogniser
import cv2
import numpy as np  
from PIL import Image                                                                  #used for capturing images


recognizer=cv2.face.LBPHFaceRecognizer_create()
path='dataSet'                                                                         #sets up a path from where images are to be compared

def getImagesWithID(path):                                                             #defining a function

    imagePaths=[os.path.join(path,f) for f in os.listdir(path)]                        #list of directories from the path, in this case images
    faces = []
    IDs = []

    for imagePath in imagePaths:

        faceImg = Image.open(imagePath).convert('L');                                   #open the image and convert it into grayscale using PIL
        faceNp = np.array(faceImg,'uint8')                                              #coverting PIL to Np
        ID = int(os.path.split(imagePath)[-1].split(".")[1])
        faces.append(faceNp)

        print(imagePath)
        print(faces)
        print(ID)
        IDs.append(ID)
        cv2.imshow("training", faceNp)
        cv2.waitKey(10)
        
    return( IDs, faces)

Ids,faces= getImagesWithID(path)
recognizer.train(faces,np.array(Ids))
recognizer.save('trainingData.yml')
cv2.destroyAllWindows()
