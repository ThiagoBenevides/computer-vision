import cv2
import numpy
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array

haarcascade =cv2.CascadeClassifier("frontalface_alt.xml")
classificador = load_model("modelo_faces.h5",compile=False)

expressoes = ["Raiva","Nojo","Medo","Feliz","Triste","Surpreso","Neutro"]
captura = cv2.VideoCapture(0)

while True:
    ret,frame = captura.read()
    cinza = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = haarcascade.detectMultiScale(cinza,scaleFactor=1.3,minNeighbors=3,minSize=(30,30))
    if len(faces)>0:
        for (x,y,w,h) in faces:
            interesse = cinza[y:y+h,x:x+w]
            interesse =cv2.resize(interesse,(48,48))
            interesse = interesse.astype("float")/255.0
            interesse = img_to_array(interesse)
            interesse = np.expand_dims(interesse,axis=0)
            previsor = classificador.predict(interesse)[0]
            rotulo = expressoes[previsor.argmax()]
            print(rotulo)
    else:
        print("Face não detectada")

captura.release()
cv2.destroyAllWindows()