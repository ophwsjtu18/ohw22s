from aip import AipSpeech
import os
import time

APP_ID = '25496064'
API_KEY = "A6fXM6nA1B8GY2txDIUCXYyu"
SECRET_KEY = "4qb3jX1C8ue1rhwMkp27kzmrxLTli9G8" 


client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

voice=client.synthesis("你好，你要吃什么？",'zh',6,{'vol':15,'per':3,'spd':5})
print("你好，你要吃什么？")
with open("C:/Users/DHW/Desktop/KaiYuanChuangKeShiJian/KC220427/Wav_A_1.wav",'wb') as fp:
    fp.write(voice)
os.system("C:/Users/DHW/Desktop/KaiYuanChuangKeShiJian/KC220427/Wav_A_1.wav")
time.sleep(3)


with open('C:/Users/DHW/Desktop/KaiYuanChuangKeShiJian/KC220427/Wav_B_1.wav', 'rb') as fp:
        wave=fp.read()
print("* 正在识别(1)......",len(wave))
result = client.asr(wave, 'wav', 16000, {'dev_pid':1536})
print(result)
if result["err_no"] == 0:
    for t in result["result"]:
        print(t)
else:
    print("没有识别到语音\n",result["err_no"])

time.sleep(3)

voice=client.synthesis("好的，麻婆豆腐菜谱如下：先                      ",'zh',6,{'vol':15,'per':3,'spd':5})
print("好的，麻婆豆腐菜谱如下：先                 ")
with open("C:/Users/DHW/Desktop/KaiYuanChuangKeShiJian/KC220427/Wav_A_2.wav",'wb') as fp:
    fp.write(voice)
os.system("C:/Users/DHW/Desktop/KaiYuanChuangKeShiJian/KC220427/Wav_A_2.wav")

time.sleep(5.5)

voice=client.synthesis("你好，你要吃什么？",'zh',6,{'vol':15,'per':3,'spd':5})
print("你好，你要吃什么？")
with open("C:/Users/DHW/Desktop/KaiYuanChuangKeShiJian/KC220427/Wav_A_3.wav",'wb') as fp:
    fp.write(voice)
os.system("C:/Users/DHW/Desktop/KaiYuanChuangKeShiJian/KC220427/Wav_A_3.wav")

time.sleep(4)

with open('C:/Users/DHW/Desktop/KaiYuanChuangKeShiJian/KC220427/Wav_B_2.wav', 'rb') as fp:
        wave=fp.read()
print("* 正在识别(1)......",len(wave))
result = client.asr(wave, 'wav', 16000, {'dev_pid':1536})
print(result)
if result["err_no"] == 0:
    for t in result["result"]:
        print(t)
else:
    print("没有识别到语音\n",result["err_no"])

