import numpy as np 
import cv2
import random
import time
from paho.mqtt import client as mqtt_client
import mediapipe as mp

# mqtt initialize
broker = 'broker.emqx.io'
port = 1883
topic = "suibiaoxieleyige"
client_id = 'python-mqtt-{random.randint(0, 1000)}'

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

mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# capture image
cap = cv2.VideoCapture(0)
with mp_hands.Hands(
    model_complexity=0,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5) as hands:
  while cap.isOpened():
    success, image = cap.read()
    if not success:
      print("Ignoring empty camera frame.")
      # If loading a video, use 'break' instead of 'continue'.
      continue

    # To improve performance, optionally mark the image as not writeable to
    # pass by reference.
    image.flags.writeable = False
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
    results = hands.process(image)

    # Draw the hand annotations on the image.
    image.flags.writeable = True
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            mp_drawing.draw_landmarks(
            image,
            hand_landmarks,
            mp_hands.HAND_CONNECTIONS,
            mp_drawing_styles.get_default_hand_landmarks_style(),
            mp_drawing_styles.get_default_hand_connections_style())
            if (hand_landmarks.landmark[8].x>hand_landmarks.landmark[5].x+0.1):
                msg = "left"
                time.sleep(1)
                result = client.publish(topic, msg)
                print(result)
            if (hand_landmarks.landmark[8].x<hand_landmarks.landmark[5].x-0.1):
                msg = "right"
                time.sleep(1)
                result = client.publish(topic, msg)
                print(result)
            if (hand_landmarks.landmark[8].y>hand_landmarks.landmark[5].y+0.08):
                msg = "down"
                time.sleep(1)
                result = client.publish(topic, msg)
                print(result)
            if (hand_landmarks.landmark[8].y<hand_landmarks.landmark[5].y-0.08):
                msg = "up"
                time.sleep(1)
                result = client.publish(topic, msg)
                print(result)
            #bu zhi dao wei sha wo de z zhou zong shi shi bie de bu shi hen ok~
            if (hand_landmarks.landmark[8].z>hand_landmarks.landmark[5].z+0.01):
                msg = "forward"
                time.sleep(1)
                result = client.publish(topic, msg)
                print(result)
            if (hand_landmarks.landmark[8].z<hand_landmarks.landmark[5].z-0.01):
                msg = "back"
                time.sleep(1)
                result = client.publish(topic, msg)
                print(result)
            #hao qi ~
            #print(hand_landmarks.landmark[8].x," ",hand_landmarks.landmark[8].y," ",hand_landmarks.landmark[5].z,"  ",hand_landmarks.landmark[5].x," ",hand_landmarks.landmark[5].y," ",hand_landmarks.landmark[5].z)
    # Flip the image horizontally for a selfie-view display.
    cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
    
    if cv2.waitKey(5) & 0xFF == 27:
        break

cv2.waitKey(0)
cv2.destroyAllWindows()