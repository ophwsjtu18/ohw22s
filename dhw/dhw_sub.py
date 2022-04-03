import random
import time
from paho.mqtt import client as mqtt_client

import numpy as np
import cv2
import mcpi.minecraft as MC 
mc = MC.Minecraft.create()
pos = mc.player.getTilePos()

broker = 'broker.emqx.io'
port = 1883
topic = "ysyyds"
client_id = f'python-mqtt-{random.randint(0, 1000)}'


def on_connect(client, userdata, flags, rc):
    if rc == 0:
        print("Connected to MQTT Broker!")
    else:
        print("Failed to connect, return code %d\n", rc)

client = mqtt_client.Client(client_id)
client.on_connect = on_connect
client.connect(broker, port)


def on_message(client, userdata, msg):
    print(f"Received {msg.payload.decode()} from {msg.topic} topic")
     
    Msg = str(msg.payload.decode())
      

    if Msg =="left":
        mc.player.setTilePos(pos.x-1,pos.y,pos.z)
        print("L")
    else:
          if Msg =="right":
            mc.player.setTilePos(pos.x+1,pos.y,pos.z)
            print("R")
          else:
              if Msg =="forword":
                mc.player.setTilePos(pos.x,pos.y,pos.z+1)
                print("F")
              else:
                  if Msg =="back":
                   mc.player.setTilePos(pos.x,pos.y,pos.z-1)
                   print("B")

                  
    #mc.player.setTilePos(pos.x+int((width*10-20*x)/width),pos.y+int((height*10-20*y)/height),pos.z+int((width*10-30*w)/width))
      
client.subscribe(topic)
client.on_message = on_message
client.loop_forever()


