from mcpi.minecraft import Minecraft
import time

def house(x0,y0,z0,L,W,H,mat,roofname):
    f=open(roofname,'r')
    roof = []

    while True:
        line = f.readline().strip()
        if line == '':
            break
        linespd = line.split(',')
        lineint = list(map(int,linespd))
        roof.append(lineint)

    #build wall
    for b in range(W):
        for a in range(L):
            mc.setBlock(x0+a, y0+b, z0, mat)
            mc.setBlock(x0+a, y0+b, z0+9, mat)
        for a in range(W-2):
            mc.setBlock(x0, y0+b, z0+1+a, mat)
            mc.setBlock(x0+9, y0+b, z0+1+a, mat)

    for a in range(L):
        for c  in range(W):
            mc.setBlock(x0+a, y0, z0+c, mat)
            mc.setBlock(x0+a, y0+9, z0+c, mat)

    #build door
    mc.setBlock(x0+5, y0+1, z0,0)
    mc.setBlock(x0+5, y0+2, z0,0)
    mc.setBlock(x0+4, y0+1, z0,0)
    mc.setBlock(x0+4, y0+2, z0,0)

    #build window
    for c in range(2):
        for b in range(2): 
            mc.setBlock(x0+9, y0+b+2, z0+c+4, 20)
            mc.setBlock(x0, y0+b+2, z0+c+4, 20)

    #build roof
    for x in range(10):
        for z in range(10):
            if roof[x][z] == 0:
                mc.setBlock(x0+x,y0+H+1,z0+z,20)
            else:
                mc.setBlock(x0+x,y0+H+1,z0+z,41)

    return 0

class House():
    def __init__(self,x,y,z):
        print("hello",x,y,z)
        self.x=x
        self.y=y
        self.z=z

    def getPos(self):
        print("house pos is",self.x,self.y,self.z)


    def setDim(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h

    def build(self):
        house(self.x,self.y,self.z,self.l,self.w,self.h,5,'roof.csv')

    def isInHouse(self,x,y,z):
        if(x>self.x and x<self.x+self.l) and (z>self.z and z<self.z+self.w) and (y>self.y and y<self.y+self.h):
            return True
        else:
            return False
        
        
mc=Minecraft.create()
pos=mc.player.getTilePos()
print("player pos is",pos)
houses = []
for m in range(3):
    for n in range(3):
        house_tmp = House(pos.x+m*20,pos.y,pos.z+n*20)
        house_tmp.setDim(10,10,8)
        house_tmp.build()
        houses.append(house_tmp)

while True:
    time.sleep(2)
    pos_now = mc.player.getTilePos()

    welcome_flag = False
    for n in range(9):
        if(houses[n].isInHouse(pos_now.x,pos_now.y,pos_now.z)):
            welcome_flag = True
            break
    

    if(welcome_flag):
        mc.postToChat("welcome home")
    else:
        mc.postToChat("please go home")

