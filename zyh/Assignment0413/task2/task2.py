from mcpi.minecraft import Minecraft
import mcpi.block as block
import cv2
import time

img = cv2.imread("pic.jpg")
W = 50
H = 50
img = cv2.resize(img, (W,H), interpolation=cv2.INTER_NEAREST)
img=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
f=open("pic.csv",'w')
for i in range(H):
    for j in range(W):
        #f.write(f"{int(img[i][j]/64)}")
        if img[i][j]>=220:
            f.write('0')
        elif img[i][j]>170:
            f.write('1')
        elif img[i][j]>70:
            f.write('2')
        else:
            f.write('3')

        if(j==W-1):
            f.write('\n')
        else:
            f.write(',')
f.close()

f=open("pic.csv",'r')
datatext = f.read()
f.close()
lines = datatext.split('\n')
data = []
for h in range(H):
    data.append(lines[h].split(','))
material = [0,8,7,15]
mc=Minecraft.create()
pos=mc.player.getTilePos()

for h in range(H):
    for w in range(W):
        mc.setBlock( pos.x+h, pos.y+W-w, pos.z, 35, material[int(data[w][h])])
