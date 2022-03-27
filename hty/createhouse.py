from mcpi.minecraft import Minecraft
import time

mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)

def house(x0,y0,z0,L,W,H,mat):
    for b in range(W):
        for a in range(L):
            mc.setBlock(x0+a, y0+b, z0, mat)
            mc.setBlock(x0+a, y0+b, z0+9, mat)
        for a in range(W-2):
            mc.setBlock(x0, y0+b, z0+1+a, mat)
            mc.setBlock(x0+9, y0+b, z0+1+a, mat)

    for a in range(L):
        for c  in range(W):
            mc.setBlock(x0+a, y0, z0+c, mat)
            mc.setBlock(x0+a, y0+9, z0+c, mat)

    mc.setBlock(x0+5, y0+1, z0,0)
    mc.setBlock(x0+5, y0+2, z0,0)
    mc.setBlock(x0+4, y0+1, z0,0)
    mc.setBlock(x0+4, y0+2, z0,0)

    for c in range(2):
        for b in range(2): 
            mc.setBlock(x0+9, y0+b+2, z0+c+4, 20)
            mc.setBlock(x0, y0+b+2, z0+c+4, 20)

    return 0

for m in range(3):
    for n in range(3):   
        house(pos.x+m*20,pos.y,pos.z+n*20,10,10,8,5)



