# -*- coding: utf-8 -*-
import numpy as np
import cv2

#Inicia a captura de video pela webcam
cap = cv2.VideoCapture(0)

while(True):
        
    _, frame = cap.read()    
    
    #RGB to HSV
    hsvFrame = cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
    
    #intervalo de Amarelo minimo e maximo
    lowerY = np.array([25, 160, 50])
    upperY = np.array([50, 255, 255])
    
    #Criando uma mascara para identificação do objeto
    mask = cv2.inRange(hsvFrame, lowerY, upperY)
    
    contours,_ = cv2.findContours(mask, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #Se existir contorno
    if(contours):
        #Pega a área do primeiro contorno
        maxArea = cv2.contourArea(contours[0])
        idContourMaxArea = 0
        i = 0
        for cnt in contours:
            #Pega o contorno que tiver a maior área
            if maxArea < cv2.contourArea(cnt):
                maxArea = cv2.contourArea(cnt)
                idContourMaxArea = i
            i += 1
        #Calcular um retângulo que envolve o objeto
        x, y, w, h = cv2.boundingRect(contours[idContourMaxArea])        
        if(maxArea > 100.0):
            #Desenhar o retângulo 
            cv2.rectangle(frame, (x,y), (x+w,y+h), (0,0,255), 3)
    
    #Mostrando na tela
    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    
    #Função para controlar o laço    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

#Desligando webcam
cap.release()
cv2.destroyAllWindows()
