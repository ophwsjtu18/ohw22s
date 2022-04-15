from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=(145,-1,-32)
#pos=mc.player.getTilePos()
f=open("C:/Users/DHW/Desktop/KaiYuanChuangKeShiJian/block2.csv",'w')
L=12
W=11
H=11
for y in range (H):
    for x in range (L):
        for z in range (W):
            block=mc.getBlockWithData(pos[0]+x,pos[1]+y,pos[2]+z)
            f.write(str(block.id))
            f.write('|')
            f.write(str(block.data))
            if z < W-1:
                f.write(',')
        f.write('\n')
        print(x,y)
f.close()
