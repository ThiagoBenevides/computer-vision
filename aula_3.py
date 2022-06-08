import cv2
import numpy as np
from aula_1 import carrega_imagem, exibi_imagem

imagem = carrega_imagem("cachorro.jpg")
linha, coluna = imagem.shape[:2]
#print(f"linha:{linha}\n Coluna:{coluna}")

#captura linha coluna


def captura_linha_coluna(imagem):
    linha, coluna = imagem.shape[:2]
    return (linha, coluna)

linha, coluna = captura_linha_coluna(imagem)



#Translação
def translacao(imagem, matriz_translacao,tamanho_caixa):

    imagem_transladada = cv2.warpAffine(imagem, matriz_translacao,tamanho_caixa,cv2.INTER_LINEAR)
    return imagem_transladada


#Rotação

def rotacao(imagem,matriz_rotacao,tamanho_caixa):
    imagem_rotacionada = cv2.warpAffine(imagem, matriz_rotacao, tamanho_caixa)
    return imagem_rotacionada




#Resize

def resize(imagem,escala,linha,coluna):
    altura = int((linha*escala)/100)
    largura= int((coluna*escala)/100)
    dimensao = (altura,largura)
    imagem_redimensionada = cv2.resize(imagem,dimensao,cv2.INTER_AREA)
    return imagem_redimensionada


redim= resize(imagem,25,linha,coluna)
