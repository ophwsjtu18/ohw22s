import random
import time
from paho.mqtt import client as mqtt_client
import mcpi.minecraft as MC 

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

    mc = MC.Minecraft.create()
    pos=mc.player.getTilePos()
    if (str(msg.payload.decode("utf-8"))=="left"):
        mc.player.setTilePos(pos.x-1,pos.y,pos.z)
    if (str(msg.payload.decode("utf-8"))=="right"):
        mc.player.setTilePos(pos.x+1,pos.y,pos.z)
    if (str(msg.payload.decode("utf-8"))=="up"):
        mc.player.setTilePos(pos.x,pos.y+1,pos.z)
    if (str(msg.payload.decode("utf-8"))=="down"):
        mc.player.setTilePos(pos.x,pos.y-1,pos.z)
    if (str(msg.payload.decode("utf-8"))=="forward"):
        mc.player.setTilePos(pos.x,pos.y,pos.z+1)
    if (str(msg.payload.decode("utf-8"))=="back"):
        mc.player.setTilePos(pos.x,pos.y,pos.z-1)

client.subscribe(topic)
client.on_message = on_message
client.loop_forever()
