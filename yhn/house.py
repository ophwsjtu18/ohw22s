import mcpi.minecraft as minecraft
import mcpi.block as block
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
def house(x0,y0,z0,length,width,height,material):
    for y in range(height):
        for a in range(length):
            mc.setBlock(x0+a, y0+y, z0, material)
            mc.setBlock(x0+a, y0+y, z0+9, material)
        for a in range(width-2):
            mc.setBlock(x0, y0+y, z0+1+a, material)
            mc.setBlock(x0+9, y0+y, z0+1+a, material)
    for x in range(length):
        for z  in range(width):
            mc.setBlock(x0+x, y0, z0+z, material)
    for x in range(length):
        for z  in range(width):
            mc.setBlock(x0+x, y0+height-1, z0+z, material)
    mc.setBlock(x0+5, y0+1, z0,0)
    mc.setBlock(x0+5, y0+2, z0,0)
    for z in range(2):
        for y in range(2): 
            mc.setBlock(x0+length-1, y0+y+2, z0+z+4, 20)
for i in range(3):
    for j in range(3):
        house(pos.x+20*i,pos.y,pos.z+20*j,10,10,8,block.STONE.id)