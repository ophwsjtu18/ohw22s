import cv2
import mediapipe as mp
from math import sqrt 
from paho.mqtt import client as mqtt_client
import random
import time

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

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands()
mpDraw = mp.solutions.drawing_utils


def getDis(x1,y1,x2,y2):
    return sqrt((x1-x2)**2+(y1-y2)**2)

x7,y7 = x8,y8 = 0,0

while True:
    img= cv2.flip(cap.read()[1],1)
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)

    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            for id, lm in enumerate(handLms.landmark):
                h, w, c = img.shape
                cx, cy = int(lm.x*w), int(lm.y*h)


                if id == 8:
                    x8,y8 = cx, cy 
                if id == 7:
                    x7,y7 = cx,cy                     
                if x8 < x7 and abs(y8 - y7) <= 10:
                    msg = "left"
                if x7 < x8 and abs(y8 - y7) <= 10:
                    msg = "right"
                if y8 < y7 and abs(x7 - x8) <= 10:
                    msg = "forward"
                if y8 > y7 and abs(x7 - x8) <=10:
                    msg = "backward"
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
    cv2.imshow("image", img)
    time.sleep(1)
    result = client.publish(topic, msg)
    if cv2.waitKey(2) & 0xFF == 27:
        break

cap.release()





