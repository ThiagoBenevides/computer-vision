#pip install opencv-python

import cv2

def carrega_imagem(caminho):
    imagem = cv2.imread(caminho)
    return imagem


def exibi_imagem(texto, figura):
    cv2.imshow(texto,figura)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


def carrega_video(caminho):
    captura = cv2.VideoCapture(caminho)
    return captura

def exibi_video(texto,captura):
    while True:
        ret, frame =captura.read()
        cv2.imshow("Video", frame)

        if cv2.waitKey(2) & 0xFF== ord('q'):
            break

    captura.release()
    cv2.destroyAllWindows()

#video = carrega_video(0)
#exibi_video("Webcam",video)