import mcpi.minecraft as minecraft
import mcpi.block as block
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
def house(x,y,z,w,h,m):
    mc.setBlocks(x,y+h+1,z,x+w,y+h+1,z+w,block.STONE_SLAB_DOUBLE)
    mc.setBlocks(x-1,y+h,z-1,x+w+1,y+h,z+w+1,block.STONE_SLAB_DOUBLE)
    mc.setBlocks(x,y,z,x+w,y+h,z+w,m)
    mc.setBlocks(x+1,y+1,z+1,x+w-1,y+h-1,z+w-1,block.AIR.id)
    mc.setBlocks(x+2,y+2,z,x+5,y+h-2,z,block.GLASS.id)
    mc.setBlocks(x,y+1,z+3,x,y+3,z+4,block.AIR.id)
    mc.setBlocks(x, y+3, z + 6, x, y + 5, z + 8, block.GLASS.id)
material=[block.STONE.id,block.WOOD_PLANKS.id,block.BRICK_BLOCK.id,block.DIRT.id,block.GOLD_BLOCK.id,block.DIAMOND_BLOCK.id,block.IRON_BLOCK.id,block.COBBLESTONE.id,
          block.CLAY.id,block]
i=l=0
for _ in range(3):
    house(pos.x+l,pos.y,pos.z,10,8,material[i])
    house(pos.x+l,pos.y,pos.z+15,10,8,material[i+1])
    house(pos.x+l,pos.y,pos.z+30,10,8,material[i+2])
    i+=3;l+=15
