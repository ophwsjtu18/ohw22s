from mcpi.minecraft import Minecraft
mc=Minecraft.create()
pos=mc.player.getTilePos()
import mcpi.block as block
name1 = "kevinroof.csv"
name2 = "roof1.csv"
import math
def house(x0,y0,z0,L,W,H,M,roofname):
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
    f = open(roofname,"r")
    roof = []
    while True:
        line = f.readline().strip()
        if line =="":
            break
        linespd = line.split(",")
        lineint = list(map(int,linespd))
        roof.append(lineint)

    for x in range(L-1):
        for z  in range(W):
            if roof[x][z]:
                print("I will setBlock with mud")
                mc.setBlock(x0+x,y0+H,z0+z,57)
            else:
                print("I will setBlock with Gold")
                mc.setBlock(x0 + x,y0+H,z0+z,20)

     #窗
    for z in range(2):
        for y in range(2): 
                mc.setBlock(x0+9, y0+y+2, z0+z+4, 20)
    #门
    for y in range(3):
        for z in range(2):
            mc.setBlock(x0 , y0 + y + 1, z0 + z + 3, 0)
print("hello")

class House():
    def __init__(self,x,y,z):
        print("hello",x,y,z)
        self.x=x
        self.y=y
        self.z=z
    def getPos(self):
        print(" house pos is ",self.x,self.y,self.z)
        return (self.x,self.y,self.z)
    def setDim(self,l,w,h,name):
        self.l=l
        self.w=w
        self.h=h
        self.name = name
    def build(self):
        print("I will build house on",self.x,self.y,self.z)
        print("hosue dimension is",self.l,self.w,self.h)
        house(self.x,self.y,self.z,self.l,self.w,self.h,1,self.name)


r=50

houses=[]
for x in range(9):
    house1= House(pos.x + r * math.cos(x * 40)  ,pos.y, pos.z + r * math.sin(x * 40))
    house1.setDim(10,10,6,name1)
    house1.build()
    houses.append(house1)

house1 = House(pos.x,pos.y,pos.z)
house1.setDim(30,30,12,name2)
house1.build()
houses.append(house1)
while True:
    for houseXX in houses:
        pos=mc.player.getTilePos()
        pos1 = houseXX.getPos()
        if pos.x > pos1[0] and pos.x < pos1[0] + 10 and pos.z > pos1[2] and pos.z<pos1[2]+ 10:
            mc.postToChat("welcome home")