# 灰度图像数字化
import cv2
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc=Minecraft.create()
pos=(6,0,-59)
img = cv2.imread('touxiang1.png', cv2.IMREAD_GRAYSCALE)   
img=cv2.resize(img,(24,32))
print(img)  
#cv2.imshow('img', img)  
for i in range(32):
    for j in range(24):
        if img[i][j]>150:
            mc.setBlock(pos[0],pos[1]+j,pos[2]+i,block.WOOL.id,0)
        if (img[i][j]<=200)and(img[i][j]>100):
            mc.setBlock(pos[0],pos[1]+j,pos[2]+i,block.WOOL.id,7)
        if img[i][j]<100:
            mc.setBlock(pos[0],pos[1]+j,pos[2]+i,block.WOOL.id,15)        
cv2.waitKey(0)
cv2.destroyAllWindows()