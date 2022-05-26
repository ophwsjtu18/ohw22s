import time
import paho.mqtt.client as mqtt


class MXMqtt():
    def __init__(self, host, post):
        self.host = host
        self.post = post
        self.mqttClient = mqtt.Client()
        self.message = None
        self.flag = False
        self._connect()

    def _connect(self):
        self.mqttClient.connect(self.host, self.post, 60)
        self.mqttClient.loop_start()

    def messageBack(self, client, userdata, msg):
        self.message = msg
        self.flag = True

    def PUB(self, topic, payload, qos = 1):
        self.mqttClient.publish(topic, payload, qos)
        time.sleep(0.1)
    
    def SUB(self, topic, qos = 1):
        self.mqttClient.subscribe(topic, qos)
        self.mqttClient.on_message = self.messageBack

    def returnMsg(self):
        if self.flag == True:
            self.flag = False
            return self.message.payload.decode("utf-8"), self.message.topic
              


if __name__ == "__main__":
    MQTTHOST = "mqtt.16302.com"
    MQTTPORT = 1883

    mqtt = MXMqtt(MQTTHOST,MQTTPORT)

    topic = "mooc12345"
    
    mqtt.SUB(topic)

    while True:
        mqtt.PUB(topic,input("输入："))
        msg = mqtt.returnMsg()
        print(msg[1]+": "+msg[0])
