# -*- coding: utf-8  -*-

import cv2
import mediapipe as mp
from math import sqrt 
from mcpi.minecraft import Minecraft
import random
import time
from paho.mqtt import client as mqtt_client
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils
broker = 'broker.emqx.io'
port = 1883
topic = "ycywj"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)




def on_message(client, userdata, msg):
    print(f"Received {msg.payload.decode()} from {msg.topic} topic")
client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)
client.subscribe(topic)
client.on_message = on_message
client.loop_forever()

def getDis(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

x4,y4 = x8,y8 = 0,0

X1,Y1 = 100,100
X2,Y2 = 100,300
X3,Y3 = 100,500

while True:
    img= cv2.flip(cap.read()[1],1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)


                if id == 4:
                    x4,y4 = cx, cy 
                if id == 8:
                    x8,y8 = cx, cy 

                if x8<200:
                    print("left")
                    mc.player.setTilePos(pos.x+1,pos.y,pos.z)
                if x8 > 400:
                    print("right")
                    mc.player.setTilePos(pos.x-1,pos.y,pos.z)
                if y8<100:
                    print("forward")
                    mc.player.setTilePos(pos.x,pos.y,pos.z+1)
                if y8>300:
                    print("back")
                    mc.player.setTilePos(pos.x,pos.y,pos.z-1)

                cv2.putText(img, str(int(id)), (cx+10, cy+10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)
            cv2.line(img,(x4,y4),(x8,y8),(100,100,200),2)
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)

    cv2.circle(img,(X1,Y1),100,(100,100,200),-1)
    cv2.circle(img,(X2,Y2),100,(100,200,200),-1)
    cv2.circle(img,(X3,Y3),100,(200,100,200),-1)
            
    cv2.imshow("image", img)
    if cv2.waitKey(2) & 0xFF == 27:
        break

cap.release()
