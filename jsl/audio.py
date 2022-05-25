from aip import AipSpeech
import os
import pyaudio
import wave
from xpinyin import Pinyin

APP_ID = '25496064'
API_KEY = "A6fXM6nA1B8GY2txDIUCXYyu"
SECRET_KEY = "4qb3jX1C8ue1rhwMkp27kzmrxLTli9G8" 
# you yu shi ming ren lian shi bie bu tong guo, wo mei you na dao mian fei zhang hao:(
client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

while 1:

    # ask
    voice=client.synthesis("你好，你要吃什么",'zh',6,{'vol':15,'per':3,'spd':5})
    with open("diyiju.mp3",'wb') as fp:
        fp.write(voice)
    os.system("diyiju.mp3")

    # answer
    CHUNK = 1024
    FORMAT = pyaudio.paInt16
    CHANNELS = 2
    RATE = 8000
    RECORD_SECONDS = 10
    WAVE_OUTPUT_FILENAME = "audio.wav"

    p = pyaudio.PyAudio()

    stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

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

    # listen
    p=Pinyin()
    flag=False
    caiming=""
    with open('audio.wav', 'rb') as fp:
        wavee=fp.read()
    print("正在识别......",len(wavee))
    result = client.asr(wavee, 'wav', 16000, {'dev_pid':1536})
    print(result)
    if result["err_no"] == 0:
        for t in result["result"]:
            print(t)
            pt=p.get_pinyin(t)
            if t=="chi":
                flag=True
            if flag:
                caiming=caiming+t
    else:
        print("没有识别到语音\n",result["err_no"])

    # comprehend
    if flag:
        daan="好的，"+caiming+"菜谱是：。。。"
        voice=client.synthesis(daan,'zh',6,{'vol':15,'per':3,'spd':5})
        with open("huida.mp3",'wb') as fp:
            fp.write(voice)
        os.system("huida.mp3")
