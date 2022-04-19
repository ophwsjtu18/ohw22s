import cv2
from mcpi.minecraft import Minecraft
import mcpi.block as block

gray = cv2.imread("cat2.jpeg", cv2.IMREAD_GRAYSCALE)   
img=cv2.resize(gray,(64,64),interpolation=cv2.INTER_CUBIC)

mc=Minecraft.create()
pos=mc.player.getTilePos()
 

cv2.imshow('img', img)  
for i in range(63):
    for j in range(63):
        bitGray = int(img[i][j] / 25)
        mc.setBlock(pos.x,pos.y+(63-i),pos.z+j,block.WOOL.id,bitGray)

        
cv2.waitKey(0)
cv2.destroyAllWindows()
