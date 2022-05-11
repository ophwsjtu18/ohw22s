from aip import AipSpeech
import pyaudio
import wave
import os

APP_ID = '25496064'
API_KEY = "A6fXM6nA1B8GY2txDIUCXYyu"
SECRET_KEY = "4qb3jX1C8ue1rhwMkp27kzmrxLTli9G8"

client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

CHUNK = 1024
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 8000
RECORD_SECONDS = 5
WAVE_OUTPUT_FILENAME = "audio.wav"

p = pyaudio.PyAudio()

stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

voice=client.synthesis("今天吃啥？",'zh',6,{'vol':15,'per':3,'spd':5})
with open("temp0.mp3",'wb') as fp:
    fp.write(voice)
os.system("temp0.mp3")

stream.start_stream()
print("* 开始录音......")

frames = []
for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
    data = stream.read(CHUNK)
    frames.append(data)

stream.stop_stream()

wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
wf.setnchannels(CHANNELS)
wf.setsampwidth(p.get_sample_size(FORMAT))
wf.setframerate(RATE)
wf.writeframes(b''.join(frames))
wf.close()

with open('audio.wav', 'rb') as fp:
        wave=fp.read()

print("* 正在识别......",len(wave))
result = client.asr(wave, 'wav', 16000, {'dev_pid':1536})

# print(result)

if result["err_no"] == 0:
    for t in result["result"]:
        print(t)
else:
    print("没有识别到语音\n",result["err_no"])


answer1="这就为您搜索"+str(result['result'])+"的菜谱"

voice=client.synthesis(answer1,'zh',6,{'vol':15,'per':3,'spd':5})
with open("temp0.mp3",'wb') as fp:
    fp.write(voice)
os.system("temp0.mp3")

print(result['result'])
b=str(result['result'][0].encode('utf-8'))
b=b[2:-1]
string=b.replace('\\x','%')
print(string)

website='https://cn.bing.com/search?q='+string+'&form=QBLH&sp=-1&pq='+string+'&sc=8-3&qs=n&sk=&cvid=9599980DDE5444178FF8AB662D0EB7F5'

os.system("\"C:/Program Files/Internet Explorer/iexplore.exe\" %s"%website)
print(website)
