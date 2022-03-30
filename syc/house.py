from mcpi.minecraft import Minecraft
import mcpi.block as block
mc=Minecraft.create()
pos=mc.player.getTilePos()
print(pos)
def Cuboid(x,y,z,d1,d2,d3,id):
    mc.setBlocks(x, y, z, x + d1, y + d2, z + d3, id)
    mc.setBlocks(x + 1, y + 1, z + 1, x + d1 - 1, y + d2 - 1, z + d3 - 1, block.AIR.id)
def midCuboid(x,y,z,d1,d2,d3,id):
    Cuboid(x - d1, y, z - d3, 2 * d1, d2, 2 * d3, id)


def house(x,y,z,d1,d2,d3,id):
    Cuboid(x-d1, y, z-d3, 2*d1, d2, 2*d3, id)

    # mc.setBlocks(x + 2, y + 2, z, x + 5, y + d2 - 2, z, block.GLASS.id)
    # mc.setBlocks(x, y + 1, z + 3, x, y + 3, z + 4, block.AIR.id)
    # mc.setBlocks(x, y + 3, z + 6, x, y + 5, z + 8, block.GLASS.id)

house(pos.x,pos.y,pos.z,3,5,3,47)

