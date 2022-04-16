//copy:
from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
f=open("block.csv",'w')
L=25
W=70
H=40
for y in range (H):
    for x in range (W):
        for z in range (L):
            block=mc.getBlockWithData(pos.x+x+1,pos.y+y,pos.z+z+1)
            f.write(str(block.id))
            f.write('|')
            f.write(str(block.data))
            if z < W-1:
                f.write(',')
            print(z,x,y)
        f.write('\n')
    f.write('.')
f.close()


//paste:
from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
L=25
W=70
H=40
f=open("block.csv",'r')
data = f.read()
block_y=data.split('.')
for y in range(H):
    block_yx=block_y[y].split('\n')
    for x in range(W):
        block_z=block_yx[x].split(',')
        for z in range(L):
            blk=block_z[z].split('|')
            if (blk[0]=='' or blk[1]==''):
                continue
            else :
                if int(blk[0]==330):
                    mc.setBlock(pos.x+x,pos.y+y,pos.z+z,0)
                else:
                    mc.setBlock(pos.x+x,pos.y+y,pos.z+z,int(float(blk[0])),int(float(blk[1])))
