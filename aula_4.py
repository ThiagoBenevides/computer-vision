import cv2
from aula_1 import carrega_imagem, exibi_imagem, carrega_video,exibi_video
"""
imagem = carrega_imagem("pedestre.jpg")
cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)
#exibi_imagem("Imagem cinza", cinza)
detector = cv2.CascadeClassifier("frontalface_alt.xml")

faces = detector.detectMultiScale(cinza,scaleFactor=1.1, minNeighbors=1,minSize=(10,10))

#print(f"Número de faces detectadas:{len(faces)}")

for (x,y,w,h) in faces:
    cv2.rectangle(imagem,(x,y),(x+w,y+h),(0,255,0),5)

exibi_imagem("Faces detectadas",imagem)
"""
captura = cv2.VideoCapture(0)
detector = cv2.CascadeClassifier("frontalface_alt.xml")


while True:
    ret, frame = captura.read()
    faces = detector.detectMultiScale(frame,scaleFactor=1.1, minNeighbors=3,minSize=(10,10))

    for (x,y,w,h) in faces:
        cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),3)
        cv2.imshow("WebCam",frame)

    if cv2.waitKey(1) & 0xFF== ord("q"):
        break

captura.release()
cv2.destroyAllWindows()
