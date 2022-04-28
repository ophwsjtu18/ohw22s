from moocxing.package import MOOCXING
from aip import AipSpeech
import os
import time
APP_ID = '25496064'
API_KEY = "A6fXM6nA1B8GY2txDIUCXYyu"
SECRET_KEY = "4qb3jX1C8ue1rhwMkp27kzmrxLTli9G8" 


client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)
MX = MOOCXING.INIT()
Brain = MOOCXING.BRAIN()
def recordSTT():
    MX.media.record(6)
    return MX.speech.STT(_print=True)

def TTSPlay(text):
    MX.speech.TTS(text)
    MX.media.play()
    
voice=client.synthesis("今天吃什么",'zh',6,{'vol':15,'per':3,'spd':5})
with open("playback.mp3",'wb') as fp:
    fp.write(voice)
os.system("playback.mp3")
time.sleep(3)   
result = recordSTT()
if "宫保鸡丁" in result:
    voice=client.synthesis("好的，宫保鸡丁的菜谱是。。。",'zh',6,{'vol':15,'per':3,'spd':5})
    with open("playback.mp3",'wb') as fp:
        fp.write(voice)
    os.system("playback.mp3")
    time.sleep(2)
if "麻婆豆腐" in result:
    voice=client.synthesis("好的，麻婆豆腐的菜谱是。。。",'zh',6,{'vol':15,'per':3,'spd':5})
    with open("playback.mp3",'wb') as fp:
        fp.write(voice)
    os.system("playback.mp3")
    time.sleep(1)

