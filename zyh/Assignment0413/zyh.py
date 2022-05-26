from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
#pos=(-100,-1,150)
L=55
W=21
H=40
f=open("block.csv",'r')
data = f.read()
split_data=data.split('\n')
print(split_data[10:20])
for y in range(H):
    for x in range(L):
        for z in range(W):
            block_data=split_data[55*y+x]
            blocks=block_data.split(',')
            blk=blocks[z].split('|')
            
            mc.setBlock(pos[0]+x,pos[1]+y,pos[2]+z,int(blk[0]),int(blk[1]))