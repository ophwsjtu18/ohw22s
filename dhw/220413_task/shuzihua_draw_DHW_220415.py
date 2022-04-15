# 灰度图像数字化
import cv2
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc=Minecraft.create()
pos=(130,17,12)
img = cv2.imread('C:/Users/DHW/Desktop/touxiang.png', cv2.IMREAD_GRAYSCALE)   
print(img.shape)
img=cv2.resize(img,(480,640))
print(img)  

#cv2.imshow('img', img)  
for i in range(640):
    for j in range(480):
        if img[i][j]>150:
            mc.setBlock(pos[0],pos[1]+j,pos[2]+i,block.WOOL.id,0)
        if (img[i][j]<=200)and(img[i][j]>100):
            mc.setBlock(pos[0],pos[1]+j,pos[2]+i,block.WOOL.id,7)
        if img[i][j]<100:
            mc.setBlock(pos[0],pos[1]+j,pos[2]+i,block.WOOL.id,15)        
cv2.waitKey(0)
cv2.destroyAllWindows()