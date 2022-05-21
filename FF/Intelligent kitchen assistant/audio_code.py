from aip import AipSpeech
import os

APP_ID = '25496064'
API_KEY = "A6fXM6nA1B8GY2txDIUCXYyu"
SECRET_KEY = "4qb3jX1C8ue1rhwMkp27kzmrxLTli9G8" 


client=AipSpeech(APP_ID,API_KEY,SECRET_KEY)

voice=client.synthesis("麻辣烫",'zh',6,{'vol':15,'per':3,'spd':5})
with open("quesion.mp3",'wb') as fp:
    fp.write(voice)
os.system("question.mp3")
