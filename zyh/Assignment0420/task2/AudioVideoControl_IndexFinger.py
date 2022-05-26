import cv2
import numpy as np
import mediapipe as mp
import pyaudio
from aip import AipSpeech
import wave
import random
import time
from paho.mqtt import client as mqtt_client

APP_ID = '25496064'
API_KEY = "A6fXM6nA1B8GY2txDIUCXYyu"
SECRET_KEY = "4qb3jX1C8ue1rhwMkp27kzmrxLTli9G8"

client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

# mqtt initialize
broker = 'broker.emqx.io'
port = 1883
topic = "sjtu2022s-mccontrol02"
client_id = f"python-mqtt--{random.randint(0, 1000)}"

def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

mqttclient = mqtt_client.Client(client_id)
mqttclient.on_connect = on_connect
mqttclient.connect(broker, port)
mqttclient.loop_start()

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 2
WAVE_OUTPUT_FILENAME = "audio.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

stream.start_stream()


mp_drawing = mp.solutions.drawing_utils
mp_drawing_styles = mp.solutions.drawing_styles
mp_hands = mp.solutions.hands

# For webcam input:
# cap = cv2.VideoCapture('http://192.168.31.114:8080')
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

        # Draw the pose annotation on the image.
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
        # Flip the image horizontally for a selfie-view display.
        cv2.imshow('MediaPipe Hands', cv2.flip(image, 1))
        if cv2.waitKey(5) & 0xFF == 27:
            break

    # 检测有没有声音
        data = stream.read(CHUNK)
        wave_data = np.frombuffer(data, dtype=np.short)
        mean=np.linalg.norm(wave_data,ord=1)/2048

        #要是有声音，则识别文字，听到”发射“就发射
        if mean > 500:

            print("* 开始录音......")
            frames = []
            for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
                data = stream.read(CHUNK)
                frames.append(data)

            wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
            wf.setnchannels(CHANNELS)
            wf.setsampwidth(p.get_sample_size(FORMAT))
            wf.setframerate(RATE)
            wf.writeframes(b''.join(frames))

            with open('audio.wav', 'rb') as fp:
                wave1 = fp.read()

            print("* 正在识别......")
            result = client.asr(wave1, 'wav', 16000, {'dev_pid': 1536})
            if result["err_no"] == 0:
                words = result["result"]
                for t in words:
                    print(t)
                if words[0].find('发射') != -1:
                    print('Success!')
                    if results.multi_hand_landmarks:
                        # every hand
                        for hand_landmarks in results.multi_hand_landmarks:
                            # draw fingers
                            mp_drawing.draw_landmarks(
                                image,
                                hand_landmarks,
                                mp_hands.HAND_CONNECTIONS,
                                mp_drawing_styles.get_default_hand_landmarks_style(),
                                mp_drawing_styles.get_default_hand_connections_style())

                            # fingers[]: (x,y)
                            landmark_list = []
                            for landmark_id, finger_axis in enumerate(
                                    hand_landmarks.landmark):
                                landmark_list.append([
                                    landmark_id, finger_axis.x, finger_axis.y,
                                    finger_axis.z
                                ])
                            if landmark_list:
                                # index finger tip
                                index_finger_tip = landmark_list[8]
                                index_finger_mcp = landmark_list[5]
                                vector = [index_finger_tip[i] - index_finger_mcp[i] for i in [1, 2, 3]]

                    print('发射方位为：',vector)
                    msg = f"{1} {vector[0]} {vector[1]} {vector[2]}"
                    result = mqttclient.publish(topic, msg)

                # 爆神装
                if words[0].find('装备') != -1:
                    msg = f"{2}"
                    print("Success!")
                    result = mqttclient.publish(topic, msg)

            else:
                print("没有识别到语音")
        else:
            # 瞄准
            time.sleep(1)
            if results.multi_hand_landmarks:
                        # every hand
                for hand_landmarks in results.multi_hand_landmarks:
                            # draw fingers
                    mp_drawing.draw_landmarks(
                                image,
                                hand_landmarks,
                                mp_hands.HAND_CONNECTIONS,
                                mp_drawing_styles.get_default_hand_landmarks_style(),
                                mp_drawing_styles.get_default_hand_connections_style())

                            # fingers[]: (x,y)
                    landmark_list = []
                    for landmark_id, finger_axis in enumerate(
                                    hand_landmarks.landmark):
                                landmark_list.append([
                                    landmark_id, finger_axis.x, finger_axis.y,
                                    finger_axis.z
                                ])
                    if landmark_list:
                                # index finger tip
                        index_finger_tip = landmark_list[8]
                        index_finger_mcp = landmark_list[5]
                        vector = [index_finger_tip[i] - index_finger_mcp[i] for i in [1, 2, 3]]

                    print('瞄准方位为：',vector)
                    msg = f"{0} {vector[0]} {vector[1]} {vector[2]}"
                    result = mqttclient.publish(topic, msg)

        mean=0

        # 测试代码：按回车键等效于“喊发射”的效果
        if cv2.waitKey(5) & 0xFF == 13:
            print('Success!')
            if results.multi_hand_landmarks:
                # every hand
                for hand_landmarks in results.multi_hand_landmarks:
                    # draw fingers
                    mp_drawing.draw_landmarks(
                        image,
                        hand_landmarks,
                        mp_hands.HAND_CONNECTIONS,
                        mp_drawing_styles.get_default_hand_landmarks_style(),
                        mp_drawing_styles.get_default_hand_connections_style())

                    # fingers[]: (x,y)
                    landmark_list = []
                    for landmark_id, finger_axis in enumerate(
                            hand_landmarks.landmark):
                        landmark_list.append([
                            landmark_id, finger_axis.x, finger_axis.y,
                            finger_axis.z
                        ])
                    if landmark_list:
                        # index finger tip
                        index_finger_tip = landmark_list[8]
                        index_finger_mcp = landmark_list[5]
                        vector = [index_finger_tip[i] - index_finger_mcp[i] for i in [1, 2, 3]]

            print('发射方位为：', vector)

cap.release()