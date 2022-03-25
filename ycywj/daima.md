import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
def house(x,y,z,w,l,h,m):
    for a in range(w):
        for b in range(h):
            for c in range(l):
                mc.setBlock(x+a, y+4+b, z, m)
                mc.setBlock(x+w, y+4+b, z+c,m)
                mc.setBlock(x, y+4+b, z+c,m)
                mc.setBlock(x+a, y+4+b, z+l,m)
                mc.setBlock(x+w, y+4+b, z+l,m)
for i in range(3):
    for j in range(3):
        house(pos.x+i*12,pos.y+4,pos.z+j*12,10,10,8,6)
