from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
Len=20
Wid=20
Hei=15
f=open("block.csv",'r')
data = f.read()
split_data=data.split('\n')
print(split_data[10:20])
for j in range(Hei):
    for i in range(Len):
        for n in range(Wid):
            block_data=split_data[20*j+i]
            blocks=block_data.split(',')
            blk=blocks[n].split('|')
            if int(blk[0]==330): 
                mc.setBlock(pos.i+i,pos.j+j,pos.n+n,0)
            else:
                mc.setBlock(pos.i+i,pos.j+j,pos.n+n,int(blk[0]),int(blk[1]))
