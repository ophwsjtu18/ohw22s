import mcpi.minecraft as minecraft
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
stone = 5


def house(x0,y0,z0,L,W,H,M):
    #地基
    for x in range(L):
        for z  in range(10):
            mc.setBlock(x0+x, y0, z0+z, M)
    #墙
    for y in range(H):
        for a in range(L):
            mc.setBlock(x0+a, y0+y, z0, M)
            mc.setBlock(x0+a, y0+y, z0+W, M)
        for a in range(W):
            mc.setBlock(x0, y0+y, z0+1+a, M)
            mc.setBlock(x0+L-1, y0+y, z0+1+a, M)
    #天花板
    for x in range(L):
        for z  in range(W+ 1):
            mc.setBlock(x0+x, y0+8, z0+z, 4)
    #窗
    for z in range(2):
        for y in range(2): 
                mc.setBlock(x0+9, y0+y+2, z0+z+4, 20)
    #门
    for y in range(3):
        for z in range(2):
            mc.setBlock(x0 , y0 + y + 1, z0 + z + 3, 0)

for x in range(3):
    for z in range(3):
        house(pos.x + x * 12, pos.y,pos.z + z *12,10,10,8,stone)