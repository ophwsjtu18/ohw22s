from mcpi.minecraft import Minecraft
import mcpi.block as block

mc = Minecraft.create() 
pos = mc.player.getTilePos()
stoneid=block.STONE.id

mc.postToChat("x="+str(pos.x)+" y"+str(pos.y)+" z="+str(pos.z))

# for y in range(10):
#     for a in range(10):
#         mc.setBlock(x0+a, y0+y, z0, stoneid)
#         mc.setBlock(x0+a, y0+y, z0+9, stoneid)
#     for a in range(8):
#         mc.setBlock(x0, y0+y, z0+a+1, stoneid)
#         mc.setBlock(x0+9, y0+y, z0+a+1, stoneid)

# for x in range(10):
#     for z in range(10):
#         mc.setBlock(x0+x,y0,z0+z,stoneid)
#         mc.setBlock(x0+x,y0+9,z0+z,stoneid)

# mc.setBlock(x0+5,y0+1,z0,0)
# mc.setBlock(x0+5,y0+2,z0,0)

# for z in range(2):
#     for y in range(2):
#         mc.setBlock(x0+10,y0+y+2,z0+z+4,20)

def house(x0,y0,z0,width,length,height):
    for y in range(height):
        for a in range(width):
            mc.setBlock(x0+a, y0+y, z0, stoneid)
            mc.setBlock(x0+a, y0+y, z0+length-1, stoneid)
        for a in range(length):
            mc.setBlock(x0, y0+y, z0+a, stoneid)
            mc.setBlock(x0+width-1, y0+y, z0+a, stoneid)

    for x in range(width):
        for z in range(length):
            mc.setBlock(x0+x,y0+height-1,z0+z,stoneid)

    mc.setBlock(x0+width/2,y0,z0,0)
    mc.setBlock(x0+width/2,y0+1,z0,0)

    for z in range(2):
        for y in range(2):
            mc.setBlock(x0+width-1,y0+y+2,z0+z+4,20)


house(pos.x,pos.y,pos.z,10,10,8)

for nx in range(3):
    for nz in range(3):
        house(pos.x+nx*15,pos.y,pos.z+nz*15,10,10,8)