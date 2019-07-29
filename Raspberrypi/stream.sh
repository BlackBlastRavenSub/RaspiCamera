#!/bin/sh
ID=test       #ユーザー名
PW=1234       #パスワード
PORT=8080     #ポート番号
#320*240
SIZE_X=180
SIZE_Y=100
QUALITY=50
  #動画のサイズ（横x縦）
FPS=30        #フレームレート

#export LD_LIBRARY_PATH=/home/fi084/LastEx/mjpg-streamer/mjpg-streamer-experimental/input_raspicam.so
./mjpg-streamer/mjpg-streamer-experimental/mjpg_streamer \
  -i "./mjpg-streamer/mjpg-streamer-experimental/input_raspicam.so -x $SIZE_X -y $SIZE_Y -fps $FPS -rot 180 -q $QUALITY" \
  -o "./mjpg-streamer/mjpg-streamer-experimental/output_http.so -w ./mjpg-streamer/mjpg-streamer-experimental/www -p 8080"
