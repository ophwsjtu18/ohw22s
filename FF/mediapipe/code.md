import numpy as np
import cv2
import time
import random
import time
import mediapipe as mp

from paho.mqtt import client as mqtt_client
from math import sqrt

#
cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils

broker = 'broker.emqx.io'
port = 1883
topic = "sjtu2022s-mccontrol02"
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

#
def length(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

#
x4,y4 = x8,y8 = x12 , y12=x16 , y16=x20 , y20=0,0

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
                if id == 12:
                    x12,y12 = cx, cy 
                if id == 16:
                    x16,y16= cx, cy 
                if id == 20:
                    x20,y20= cx, cy 

                if length(x4,y4,x8,y8) <=30:
                    print("Forward")
                    msg="Forward"
                else:
                    if length(x4,y4,x12,y12)<=30:
                     print("Back")
                     msg="Back"
                    else:
                         if length(x4,y4,x16,y16)<=30:
                             print("Left")
                             msg="Left"
                         else:
                             if length(x4,y4,x20,y20)<=50:
                                 print("Right") 
                                 msg="Right"
                
                cv2.putText(img, str(int(id)), (cx+10, cy+10), cv2.FONT_HERSHEY_PLAIN, 1, (0, 0, 255), 2)

            cv2.line(img,(x4,y4),(x8,y8),(100,100,200),2)
            cv2.line(img,(x4,y4),(x12,y12),(100,100,200),2)
            cv2.line(img,(x4,y4),(x16,y16),(100,100,200),2)
            cv2.line(img,(x4,y4),(x20,y20),(100,100,200),2)
            
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cv2.imshow("image", img)
    time.sleep(0.1)
    result = client.publish(topic, msg)
    print(result)
    time.sleep(0.1)  
    
    if cv2.waitKey(2) & 0xFF == 27:
        break

#
cap.release()
destroyAllWindows()
