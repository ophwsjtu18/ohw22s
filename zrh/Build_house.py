import mcpi
import mcpi.minecraft as minecraft
mc=minecraft.Minecraft.create()
pos=mc.player.getTilePos()
x0=pos.x
y0=pos.y
z0=pos.z
def humble_house(x0,y0,z0,L,W,H,M):
    #The surrounding walls 
    for y in range(H):
        for x in range(L):
            mc.setBlock(x0+x,y0+y,z0,M)
            mc.setBlock(x0+x,y0+y,z0+L-1,M)
        for x in range(W):
            mc.setBlock(x0,y0+y,z0+x,M)
            mc.setBlock(x0+W-1,y0+y,z0+x,M)
    #The Floor
    for x in range(L):
        for z in range(W-1):
            mc.setBlock(x0+x,y0,z0+z+1,M)
    #The Ceiling
    for x in range(L):
        for z in range(W-2):
            mc.setBlock(x0+x,y0+H,z0+z+1,M)
    #The door
    mc.setBlock(x0+5,y0+1,z0,0)
    mc.setBlock(x0+5,y0+2,z0,0)
    #The Window
    for z in range(2):
        for y in range(2):
            mc.setBlock(x0+L-1,y0+y+2,z0+z+4,20)
    for x in range(2):
        for y in range(2):
            mc.setBlock(x0+x+1,y0+y+2,z0,20)
M0list=[17,89,18,16,96,
        126,119,79,91,56,
        24,29,47,82,177
        ,95,85,178,102,58,
        130,67,112,137,25,
        99,108]
M0=0
H0=8
L0=10
W0=10
for i in [0,1,2]:
    for j in [0,1,2]:
        for k in[0,1,2]:
          humble_house(x0+(L0+4)*i,y0+(H0+2)*j,z0+(W0+4)*k,L0,W0,H0,M0list[M0])
          M0=M0+1

