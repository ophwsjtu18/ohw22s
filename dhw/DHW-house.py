import mcpi.minecraft as minecraft
import mcpi.block as block

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()


def house(x,y,z,h,w,l):
   
   for b in range(w):
         for c in range(l):
              mc.setBlock(x+b, y, z+c,block.STONE.id)
 
   for a in range(h):
     for b in range(l):
        mc.setBlock(x+b,y+a, z,block.STONE.id)
        mc.setBlock(x+b,y+a, z+w-1, block.STONE.id)
    
   for a in range(h):
     for b in range(w):
        mc.setBlock(x,y+a, z+b,block.STONE.id)
        mc.setBlock(x+l-1,y+a, z+b,block.STONE.id)    
    
   for a in range(2):
      for b in range(2): 
            mc.setBlock(x,b+y+2, z+a+4, 20)
   
   for a in range(w):
      for b  in range(l):
            mc.setBlock(x+a,y+h-1, z+b,block.STONE.id)
   mc.setBlock(x+5, y+1,z,0)
   mc.setBlock(x+5, y+2, z,0)
   mc.setBlock(x+5, y+3,z,0)
   mc.setBlock(x+4, y+1, z,0)
   mc.setBlock(x+4, y+3,z,0)
   mc.setBlock(x+4, y+2, z,0)


for a in range (0,3):
    for b in range (0,3):
      house (136+13*a,60,-322+13*b,8,10,10)