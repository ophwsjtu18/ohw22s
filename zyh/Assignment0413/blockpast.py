from mcpi.minecraft import Minecraft
import mcpi.block as block
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()
#pos=(-100,-1,150)
L=100
W=100
H=50
f=open("block.csv",'r')
data = f.read()
split_data=data.split('\n')
print(split_data[10:20])
for y in range(H):
    for x in range(L):
        for z in range(W):
            block_data=split_data[L*y+x]
            blocks=block_data.split(',')
            blk=blocks[z].split('|')
            #if int(blk[0]==330):  #门拷贝要碎，设置成空气然后手搭
              #  mc.setBlock(pos[0]+x,pos[1]+y,pos[2]+z,0)
           # else:
            mc.setBlock(pos[0]+x,pos[1]+y,pos[2]+z,int(blk[1]))