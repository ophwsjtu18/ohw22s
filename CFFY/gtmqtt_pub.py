import random
import time
import numpy as np
import cv2
a=300
b=360
c=260
d=200
e=200
f=100
cap = cv2.VideoCapture(0)
from paho.mqtt import client as mqtt_client

broker = 'broker.emqx.io'
port = 1883
client_id = f'python-mqtt-{random.randint(0, 1000)}'
topic="ysyyds"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()

msg_count=0

while True:
    ret, frame = cap.read()
    if ret == True:
        frame = cv2.flip(frame, 1)
    face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
    img = frame
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        roi_gray = gray[y:y+h, x:x+w]
        roi_color = img[y:y+h, x:x+w]
    cv2.imshow('img',img)
    h=img.shape[0]
    w=img.shape[1]
    
    if(x+w/2)<a:
        msg="left"
    if(x+w/2)>b:
        msg="right"
    if(y+h/2)>c:
        msg="down"
    if(y+h/2)<d:
        msg="up"
    if w>e:
        msg="forward"
    if w<f:
        msg="back"
    if(x+w/2)>a and (x+w/2)<b and (y+h/2)<c and (y+h/2)>d and w<e and w>f:
        msg="stop"
    time.sleep(1)
    result = client.publish(topic, msg)
    print(result)
    if cv2.waitKey(1) & 0xFF == 27:
        break
cap.release()
cv2.waitKey(0)
cv2.destroyAllWindows()
