import mcpi.minecraft as MC 
mc = MC.Minecraft.create()
pos = mc.player.getTilePos()
mc.postToChat("x="+str(pos.x)+"y"+str(pos.y)+"z="+str(pos.z))
def house(x,y,z,w,l,h,m):
    for a in range(w):
        for b in range(l):
            mc.setBlock(x+a,y,z+b,m)
            mc.setBlock(x+a,y+h,z+b,m)
    for a in range(w):
        for c in range(h):
            mc.setBlock(x+a,y+c,z,m)
            mc.setBlock(x+a,y+c,z+l,m)
    for b in range(l):
        for c in range(h):
            mc.setBlock(x,y+c,z+b,m)
            mc.setBlock(x+w,y+c,z+b,m)
for i in range(3):
    for j in range(3):
        house(pos.x+12*i,pos.y,pos.z+12*j,10,10,8,1)
