import cv2
from mcpi.minecraft import Minecraft
import mcpi.block as block

mc=Minecraft.create()
pos=mc.player.getTilePos()
img = cv2.imread("C:/Users/Lenovo/Desktop/target.png", cv2.IMREAD_GRAYSCALE)   

img=cv2.resize(img,(34,34),interpolation=cv2.INTER_CUBIC)
 

cv2.imshow('img', img)  
for i in range(30):
    for j in range(30):
        temp = int(img[i][j] / 25)
        if temp == 0:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.WOOL.id,temp)
        elif temp == 1:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.WOOL.id,temp)
        elif temp == 2:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.WOOL.id,temp)
        elif temp == 3:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.WOOL.id,temp)
        elif temp ==4:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.WOOL.id,temp)
        elif temp == 5:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.WOOL.id,temp)
        elif temp == 6:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.WOOL.id,temp)
        elif temp == 7:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.WOOL.id,temp)
        elif temp == 8:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.WOOL.id,temp)
        elif temp == 9:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.WOOL.id,temp)
        elif temp == 10:
            mc.setBlock(pos.x,pos.y+j,pos.z+i,block.WOOL.id,temp)
        
 
        
cv2.waitKey(0)
cv2.destroyAllWindows()