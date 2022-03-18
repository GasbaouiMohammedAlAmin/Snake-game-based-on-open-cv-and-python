# -*- coding: utf-8 -*-
"""
Created on Sun Mar  6 22:35:42 2022

@author: amine gasa
"""
from  SnakeGameClass import *
import cv2
from cvzone.HandTrackingModule import HandDetector

cap=cv2.VideoCapture(0);
cap.set(3,1280) #the size frame
cap.set(4,1024)
detector=HandDetector(detectionCon=0.8,maxHands=1)
game=SnakeGameClass("donut.png")

while True:
    success , img=cap.read();
    img=cv2.flip(img,1)
    hands,img=detector.findHands(img,flipType =False)
    if hands:# if i detect at least one hand
        lmList=hands[0]["lmList"]
        pointIndex=lmList[8][0:2]
        img=game.update(img,pointIndex)# to update the score and the length snake
    cv2.imshow("img", img)
    
    if(cv2.waitKey(1)== ord('r')):
        game.gameOver=False
        game.score=0
    if  (cv2.waitKey(1)== ord('q')):
        break
