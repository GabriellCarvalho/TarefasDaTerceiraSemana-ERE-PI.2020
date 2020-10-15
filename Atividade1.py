# -*- coding: utf-8 -*-

import cv2
import numpy as np

#Lendo a imagem de fundo
image = cv2.imread('imagem.jpg')

#Pegando as dimensões da imagem de fundo
h, w = image.shape[:2]
image = np.dstack([image,np.ones((h,w), dtype= 'uint8')* 255])

#Lendo a marca d'água
marca = cv2.imread('python.png', cv2.IMREAD_UNCHANGED)

#Redimensionar marca d'água
marca = cv2.resize(marca,(100,100))

#Separando as camadas 
b, g, r, a = cv2.split(marca)

#Aplicando uma mascara para retirar o fundo
b = cv2.bitwise_and(b, b, mask = a)
g = cv2.bitwise_and(g, g, mask = a)
r = cv2.bitwise_and(r, r, mask = a)
marca = cv2.merge([b,g,r,a])

#Pegando as dimensões da marca d'água
marcaH, marcaW = marca.shape[:2]

#Criando uma sobreposição 
overlay = np.zeros((h,w,4), dtype='uint8')
overlay[h - marcaH:h, w - marcaW:w]= marca

#Adicionando a marca d'água
image = cv2.addWeighted(overlay, 0.4, image,1.0,0)

#Mostrado a imagem final
cv2.imshow('Imagem',image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#Salvando a nova imagem
cv2.imwrite('imagemNova.jpg',image)