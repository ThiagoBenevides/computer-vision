import cv2



def carrega_imagem(figura):
    imagem = cv2.imread(figura)
    return imagem

def exibi_imagem(texto,imagem):
    cv2.imshow(texto,imagem)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

def bgr_2_gray(imagem):
    imagem_cinza = cv2.cvtColor(imagem,cv2.COLOR_BGR2GRAY)

def bgr_2_hsv(imagem):
    imagem_hsv = cv2.cvtColor(imagem, cv2.COLOR_BGR2HSV)
    return imagem_hsv

def hsv_2_bgr(imagem):
    imagem_bgr = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2BGR)
    return imagem_bgr

def hsv_2_rgb(imagem):
    imagem_rgb = cv2.cvtColor(imagem_hsv, cv2.COLOR_HSV2RGB)
    return imagem_rgb


imagem = carrega_imagem("cachorro.jpg")
imagem_hsv = bgr_2_hsv(imagem)

exibi_imagem("Cachorro bgr",imagem_hsv)