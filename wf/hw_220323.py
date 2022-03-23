import mcpi.minecraft as minecraft
import mcpi.block as block

def house(x0,y0,z0,L,W,H,M):
    # walls
    for y in range(H):
        for a in range(L):
            mc.setBlock(x0+a, y0+y, z0, M)
            mc.setBlock(x0+a, y0+y, z0+W-1, M)
        for a in range(W-2):
            mc.setBlock(x0, y0+y, z0+1+a, M)
            mc.setBlock(x0+L-1, y0+y, z0+1+a, M)
    # floors
    for x in range(L):
        for z  in range(W):
            mc.setBlock(x0+x, y0, z0+z, M)
    for x in range(L):
        for z  in range(W):
            mc.setBlock(x0+x, y0+H-1, z0+z, block.WOOD.id)
    # door
    for x in range(3):
        for y in range(4):
            mc.setBlock(x0+L//2+x-1, y0+y+1, z0, 0)

    # window
    for z in range(2):
      for y in range(2): 
            mc.setBlock(x0, y0+y+6, z0+z+4, 20)

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
x0=pos.x
y0=pos.y
z0=pos.z
for i in range(3):
    for j in range(3):
        house(x0+15*i,y0,z0+15*j,10,8,10,block.STONE.id)
