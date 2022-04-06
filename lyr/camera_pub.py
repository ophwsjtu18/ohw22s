import numpy as np
import cv2

import time
import random
import time
from paho.mqtt import client as mqtt_client


face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

cap=cv2.VideoCapture(0)

broker = 'broker.emqx.io'
port = 1883
topic = "sjtu2022sThird-mccontrol"
client_id = f'python-mqtt-{random.randint(0, 1000)}'
msg = ""


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)
client.loop_start()


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
        if(x < 50):
            msg = "Left"
        if(x >150):
            msg = "Right"
        if(w > 300):
            msg = "Forward"
        if(w < 150):
            msg = "Backward"
    cv2.imshow('img',img)

    time.sleep(1)
    result = client.publish(topic, msg)
    print(result)
    
    if cv2.waitKey(1) & 0xFF == 27:
        break


cap.release()
cv2.destroyAllWindows()