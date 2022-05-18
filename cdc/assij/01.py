from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
f=open("block.csv",'w')
Len=20
Wid=20
Hei=15
for j in range (Hei):
    for i in range (Len):
        for n in range (Wid):
            block=mc.getBlockWithData(pos.i+i+1,pos.j+j,pos.n+n+1)
            f.write(str(block.id))
            f.write('|')
            f.write(str(block.data))
            if n < Wid -1:
                f.write(',')

        f.write('\n')
        print(i,j)
f.close()
