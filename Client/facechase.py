#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import time

from socket import socket, AF_INET, SOCK_DGRAM

HOST = ''
PORT = 5000
ADDRESS = "raspi-b070.local"
num = 1

s = socket(AF_INET, SOCK_DGRAM)
# ブロードキャストする場合は、ADDRESSを
# ブロードキャスト用に設定して、以下のコメントを外す
# s.setsockopt(SOL_SOCKET, SO_BROADCAST, 1)

width = 180
hidth = 100
URL = "http://raspi-b070.local:8080/?action=stream"
capture = cv2.VideoCapture(URL)
faceCascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')

while True:
 _, img = capture.read()
 img = cv2.resize(img, (width, hidth))
 gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 faces = faceCascade.detectMultiScale(
  gray,
  scaleFactor=1.1,
  minNeighbors=3,
  minSize=(30, 30),
  flags=cv2.CASCADE_SCALE_IMAGE
 )
 for (x, y, w, h) in faces:
  cv2.rectangle(img, (x, y), (x+w, y+h), (0, 255, 0), 2)
  #print((x+(w/2)-(width/2)),(y+(h/2)-(hidth/2)))
  Xparameter=(x+(w/2)-(width/2))
  Yparameter=(y+(h/2)-(hidth/2))  
  msgx = str(Xparameter)
  msgy = str(Yparameter)
  print(msgx)
  msg = msgx + ',' +msgy
  msg = msg.encode()
  #msg = str(Xparameter + "," + Yparameter)
  # 送信
  if num%1 == 0:
   s.sendto(msg, (ADDRESS, PORT))
   num = 1
 num=num + 1
 print(num)
 cv2.imshow("camera", img)
 #time.sleep(0.5)
 if cv2.waitKey(10) > 0:
  break
cv2.DestroyAllWindows()
s.close()
