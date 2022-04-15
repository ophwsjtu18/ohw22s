from mcpi.minecraft import Minecraft
import time
mc=Minecraft.create()
pos=mc.player.getTilePos()

L=12
W=11
H=11
f=open("C:/Users/DHW/Desktop/KaiYuanChuangKeShiJian/block2.csv",'r')
data = f.read()
split_data=data.split('\n')
print(len(split_data))

print(split_data[10:20])
for y in range(H):
    for x in range(L):
        for z in range(W):
            block_data=split_data[12*y+x]
            blocks=block_data.split(',')
            blk=blocks[z].split('|')
            if int(blk[0]==330):  #门拷贝要碎，设置成空气然后手搭
                mc.setBlock(pos[0]+x,pos[1]+y,pos[2]+z,0)
            else:
               mc.setBlock(pos.x+x,pos.y+y,pos.z+z,int(blk[0]),int(blk[1]))
