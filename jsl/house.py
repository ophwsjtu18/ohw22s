import mcpi.minecraft as minecraft
import mcpi.block as block

class House():
    def __init__(self,x,y,z):
        print("hello",x,y,z)
        self.x=x
        self.y=y
        self.z=z
    def getPos(self):
        print("house pos is",self.x,self.y,self.z)
        return(self.x,self.y,self.z)
    def setDim(self,l,w,h):
        self.l=l
        self.w=w
        self.h=h
    def setName(self,s):
        self.name=s
    def build(self,M,roofname):
        print("I will build house on",self.x,self.y,self.z)
        print("hosue dimension is", self.l, self.w,self.h)
        f=open(roofname,"r")

        roof=[]

        while True:
            line=f.readline().strip()
            if line=="":
                break
            linespd=line.split(",")
            lineint=list(map(int,linespd))
            roof.append(lineint)
        print(roof)
        # walls
        for y in range(self.h):
            for a in range(self.l):
                mc.setBlock(self.x+a, self.y+y, self.z, M)
                mc.setBlock(self.x+a, self.y+y, self.z+self.w-1, M)
            for a in range(self.w-2):
                mc.setBlock(self.x,self.y+y, self.z+1+a, M)
                mc.setBlock(self.x+self.l-1, self.y+y, self.z+1+a, M)
        # floors
        for x in range(self.l):
            for z  in range(self.w):
                mc.setBlock(self.x+x, self.y, self.z+z, M)
    
        #roof
        for i in range(self.l):
            for j in range(self.w):
                if roof[i][j]==0:
                    print("I will setBlock with mud")
                    mc.setBlock(self.x+i, self.y+self.h-1, self.z+j, block.GLASS.id)
                else:
                    print("I will setBlock with Gold")
                    mc.setBlock(self.x+i, self.y+self.h-1, self.z+j, block.GOLD_ORE.id)
    
        f.close()

        # door
        for x in range(3):
            for y in range(4):
                mc.setBlock(self.x+self.l//2+x-1, self.y+y+1, self.z, 0)

        # window
        for z in range(2):
            for y in range(2): 
                mc.setBlock(self.x, self.y+y+3, self.z+z+3, 20)
    def isInHouse(self,pos):
        if (pos.x>=self.x)and(pos.y>=self.y)and(pos.z>=self.z)and(pos.x<=self.x+self.l)and(pos.y<=self.y+self.h)and(pos.z<=self.z+self.w):
            mc.postToChat("welcome to "+self.name+" \'s home")


mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
f1=open("clan_layout.csv","r")
houses=[]
line=f1.readline().strip()
x_max=-1000
z_max=-1000
x_min=1000
z_min=1000
while True:
    line=f1.readline().strip()
    if line=="":
        break
    linespd=line.split(",")
    houselist=list(map(int,linespd[1:8]))
    #print(linespd)
    house1=House(houselist[0],houselist[1],houselist[2])
    pos1=house1.getPos()
    house1.setDim(houselist[3],houselist[4],houselist[5])
    house1.build(houselist[6],linespd[8])
    house1.setName(linespd[0])
    houses.append(house1)
    if houselist[0]-2<x_min:
        x_min=houselist[0]-2
    if houselist[2]-2<z_min:
        z_min=houselist[2]-2
    if houselist[0]+houselist[3]+2>x_max:
        x_max=houselist[0]+houselist[3]+2
    if houselist[2]+houselist[5]+2>z_max:
        z_max=houselist[2]+houselist[5]+2
for h in range(5):
    for i in range(x_min,x_max+2):
        mc.setBlock(i,h, z_min-1,  1)
        mc.setBlock(i,h, z_max+1, 1)
    for i in range(z_min,z_max+2):
        mc.setBlock(x_min-1, h,i, 1)
        mc.setBlock(x_max+1,h,i, 1)
while True:
    for i in houses:
        pos = mc.player.getTilePos()
        i.isInHouse(pos)

