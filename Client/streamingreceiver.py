#!/usr/bin/env python
# -*- coding: utf-8 -*-

import cv2
import skvideo.io #追加

URL = "http://raspi-b070.local:8080/?action=stream"
s_video = cv2.VideoCapture(URL)

while True:
  ret, img = s_video.read()
  cv2.imshow("Stream Video",img)
  key = cv2.waitKey(1) & 0xff
  if key == ord('q'): break
