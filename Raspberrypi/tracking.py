#!!
from socket import socket, AF_INET, SOCK_DGRAM

import struct
import sys
import time
import pigpio
from pantilthat import *

HOST = ''
PORT = 5000
SERVO_PIN = 4
angle_x=0
angle_y=0
reverse = False

x=0
y=0

# ソケットを用意
s = socket(AF_INET, SOCK_DGRAM)
# バインドしておく
s.bind((HOST, PORT))

while True:
    # 顔の位置情報を受信
    msg, address = s.recvfrom(8192)
    #print("msg: {}, address: {}".format(msg, address))
    msg = msg.decode()
    msg = msg.split(",")
    print(msg)
    x = float(msg[0])
    y = float(msg[1])
    print(x)
   #ここからカメラのトラッキング機能
   #まずはX軸の調整
    if x<-5 and angle_x <= 90:
        angle_x=angle_x+1
    elif x>5 and angle_x >= -90:
        angle_x=angle_x-1
    #次にY軸の調整
    if y<-5 and angle_y >= -90:
        angle_y=angle_y-1
    elif y>5 and angle_y <= 90:
        angle_y=angle_y+1
#実際にモータを動作させる
    print(angle_x)
    print(angle_y)
    pantilthat.servo_one(angle_x)
    pantilthat.servo_two(angle_y)
     #time.sleep(0.5)
# ソケットを閉じておく
s.close()
