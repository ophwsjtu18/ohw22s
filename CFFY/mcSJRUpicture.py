import numpy as np
import cv2
from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()

img=cv2.imread('profile picture.jpg')
img=cv2.resize(img,(200,300))
h,w=img.shape[:2]

for y in range (1,h):
    for z in range (1,w):
        (b,g,r)=img[y,z]
        if (b>150 and g>150):
            if (r>150):
                mc.setBlock(pos.x+10,pos.y+200-y,pos.z+z,block.WOOL.id,0)
            else :
                mc.setBlock(pos.x+10,pos.y+200-y,pos.z+z,block.WOOL.id,4)
        else :
            mc.setBlock(pos.x+10,pos.y+200-y,pos.z+z,block.WOOL.id,15)


cv2.waitKey(0)
cv2.destroyAllWindows()
