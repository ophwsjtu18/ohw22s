import mcpi.minecraft as minecraft
import mcpi.block as block
import time
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
class House():
    def __init__(self,x0,y0,z0):
        print("hello",x0,y0,z0)
        self.x0=x0
        self.y0=y0
        self.z0=z0
    def getPos(self):
        print(" house pos is ",self.x0,self.y0,self.z0)
        return (self.x0,self.y0,self.z0)
    def setDim(self,l0,w0,h0):
        self.l0=l0
        self.w0=w0
        self.h0=h0
    @property
    def x(self):
        return self.x0
    @property
    def y(self):
        return self.y0
    @property
    def z(self):
        return self.z0
    @property
    def w(self):
        return self.w0
    @property
    def h(self):
        return self.h0
    @property
    def l(self):
        return self.l0
    def build(self):
        x0=self.x0
        y0=self.y0
        z0=self.z0
        m0=self.l0
        w0=self.w0
        h0=self.h0
        for a in range(w0):
            for b in range(h0):
                for c in range(m0):
                        mc.setBlock(x0+a, y0+b, z0+c, block.TNT.id)
        for a in range(w0-2):
            for b in range(h0-2):
                for c in range(m0-2):
                        mc.setBlock(x0+a+1, y0+b+1, z0+c+1, block.AIR.id)
        for a in range(4):
            for b in range(4):
                for c in range(1):
                        mc.setBlock(x0+a+3, y0+b+1, z0+c, block.AIR.id)
        f=open("roof.csv","r")
        roof=[]
        while True:
            line=f.readline().strip()
            if line=="":
                break
            linespd=line.split(",")
            lineint=list(map(int,linespd))
            roof.append(lineint)
        print(roof)
            
        for i in range(min(w0,10)):
            for j in range(min(m0,10)):
                if roof[i][j]==0:
                     mc.setBlock(x0+i, y0+h0, z0+j, block.TNT.id)
                else:
                     mc.setBlock(x0+i, y0+h0, z0+j, block.GLOWSTONE_BLOCK.id)

        f.close()
        print("I will build house on",self.x0,self.y0,self.z0)
        print("hosue dimension is", self.l0,self.w0,self.h0)

house1=House(pos.x,pos.y,pos.z)
house2=House(pos.x+40,pos.y,pos.z)

pos1=house1.getPos()
pos2=house2.getPos()

print("two houses locate on",pos1,pos2)

house1.setDim(10,10,10)
house2.setDim(20,20,20)
house1.build()
house2.build()
i=0;
j=0;
while(True):
    pos = mc.player.getTilePos()
    if(house1.x<pos.x and house1.x+house2.w>pos.x and house1.y<pos.y and house1.y+house1.h>pos.y and house1.z<pos.z and house1.z+house1.l>pos.z and i==0):
        print("welcome home")
        i=1
    if(not(house1.x<pos.x and house1.x+house2.w>pos.x and house1.y<pos.y and house1.y+house1.h>pos.y and house1.z<pos.z and house1.z+house1.l>pos.z)):
        i=0
    if(house2.x<pos.x and house2.x+house2.w>pos.x and house2.y<pos.y and house2.y+house2.h>pos.y and house2.z<pos.z and house2.z+house2.l>pos.z and j==0):
        print("welcome home")
        j=1
    if(not(house2.x<pos.x and house2.x+house2.w>pos.x and house2.y<pos.y and house2.y+house2.h>pos.y and house2.z<pos.z and house2.z+house2.l>pos.z)):
        j=0


