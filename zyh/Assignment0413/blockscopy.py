from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
f=open("block.csv",'w')
L=100
W=100
H=50
for y in range (H):
    for x in range (L):
        for z in range (W):
            block=mc.getBlockWithData(pos.x+x,pos.y+y,pos.z+z)
            f.write(str(block.id))
            f.write('|')
            f.write(str(block.data))
            if z < W-1:
                f.write(',')
        f.write('\n')
        print(x,y)
f.close()