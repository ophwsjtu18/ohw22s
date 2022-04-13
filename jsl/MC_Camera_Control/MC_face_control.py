import cv2
import time
import numpy as np
import mcpi.minecraft as MC
mc = MC.Minecraft.create()
face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()
    img = cv2.flip(frame,1)

    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)

    pos = mc.player.getTilePos()

    for (x,y,w,h) in faces:
        img = cv2.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
        if w > 300:
            cv2.putText(img,'forword',(x,y),cv2.FONT_HERSHEY_COMPLEX, 1, (100, 200, 200), 2)
            mc.player.setTilePos(pos.x, pos.y, pos.z-1)
        elif w < 150:
            cv2.putText(img,'backword',(x,y),cv2.FONT_HERSHEY_COMPLEX, 1, (100, 200, 200), 2)
            mc.player.setTilePos(pos.x, pos.y, pos.z+1)
        elif w > 150 and w < 300 and y + h / 2 < 150:
            cv2.putText(img,'up',(x,y),cv2.FONT_HERSHEY_COMPLEX, 1, (100, 200, 200), 2)
            mc.player.setTilePos(pos.x, pos.y+1, pos.z)
        elif w > 150 and w < 300 and y + h / 2 > 350:
            cv2.putText(img,'down',(x,y),cv2.FONT_HERSHEY_COMPLEX, 1, (100, 200, 200), 2)
            mc.player.setTilePos(pos.x, pos.y-1, pos.z)
        elif w > 150 and w < 300 and x + w / 2 < 200:
            cv2.putText(img,'left',(x,y),cv2.FONT_HERSHEY_COMPLEX, 1, (100, 200, 200), 2)
            mc.player.setTilePos(pos.x-1, pos.y, pos.z)
        elif w > 150 and w < 300 and x + w / 2 > 400:
            cv2.putText(img,'right',(x,y),cv2.FONT_HERSHEY_COMPLEX, 1, (100, 200, 200), 2)
            mc.player.setTilePos(pos.x+1, pos.y, pos.z)

    cv2.imshow('img', img)

    # mc.postToChat("x="+str(pos.x)+"y="+str(pos.y)+"z="+str(pos.z))
    if cv2.waitKey(1) & 0xFF == 27:
        break


# show the image
cap.release()
cv2.destroyAllWindows() 