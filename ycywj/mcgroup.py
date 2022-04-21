# -*- coding: utf-8 -*-
import mcpi.minecraft as minecraft
import mcpi.block as block
import time
import cv2 as cv
mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()
def buildhouse(x0,y0,z0,L,W,H,M):
    for x in range(L):
        for z  in range(10):
            mc.setBlock(x0+x, y0, z0+z, M)
    for y in range(H):
        for a in range(L):
            mc.setBlock(x0+a, y0+y, z0, M)
            mc.setBlock(x0+a, y0+y, z0+W, M)
        for a in range(W):
            mc.setBlock(x0, y0+y, z0+1+a, M)
            mc.setBlock(x0+L-1, y0+y, z0+1+a, M)
    for x in range(L):
        for z  in range(W+ 1):
            mc.setBlock(x0+x, y0+8, z0+z, 4)
    for z in range(2):
        for y in range(2): 
                mc.setBlock(x0+9, y0+y+2, z0+z+4, 20)
    for y in range(3):
        for z in range(2):
            mc.setBlock(x0 , y0 + y + 1, z0 + z + 3, 0)
def buildroof(x,y,z,w,l,h,roofname):
        f=open(roofname,"r")

        roof=[]

        while True:
            line=f.readline().strip()
            if line=="":
                break
            linespd=line.split(",")
            lineint=list(map(int,linespd))
            roof.append(lineint)
        for i in range(w):
            for j in range(l):
                if roof[i][j]==0:
                    mc.setBlock(x+i, y+h, z+j+1,49)
                else:
                    mc.setBlock(x+i, y+h, z+j+1,15)
        f.close()

class House():
    def __init__(self,x,y,z,l,w,h):
        self.x=x
        self.y=y
        self.z=z
        self.l=l
        self.w=w
        self.h=h
        print("I will build a house on",self.x,self.y,self.z,self.l,self.w,self.h)
    def buildbuild(self):
        buildhouse(self.x,self.y,self.z,self.w,self.l,self.h,45)
        buildroof(self.x,self.y,self.z,self.w,self.l,self.h,"roof.csv")
    def buildhousex9(self):
        for i in range(3):
            for j in range(3):
                buildhouse(self.x+i*13,self.y,self.z+13*j,self.w,self.l,self.h,46)
                buildroof(self.x+i*13,self.y,self.z+13*j,self.w,self.l,self.h,"roof.csv")
    def ishouse(self):
        while(True):
            pos2= mc.player.getTilePos()
            if((self.x+self.w)>pos2.x&pos2.x>self.x&(self.y+self.l)>pos2.y&pos2.y>self.y):
                print("welcome to kevin house")
                break
            time.sleep(1)
    def buildwall(self):
        x0=self.x-0.6*self.l
        y0=self.y
        z0=self.z-0.6*self.w
        H=self.h*3
        L=self.l*5
        W=self.w*5
        M=21
        for y in range(H):
            for a in range(L):
                mc.setBlock(x0+a, y0+y, z0, M)
                mc.setBlock(x0+a, y0+y, z0+W, M)
            for a in range(W):
                mc.setBlock(x0, y0+y, z0+1+a, M)
                mc.setBlock(x0+L-1, y0+y, z0+1+a, M)
    def buildhall(self):
            buildhouse(self.x+13,self.y+self.h*2,self.z+13,self.w*2,self.l*2,self.h*2,41)
            buildroof(self.x+13,self.y+self.h*2,self.z+13,self.w*2,self.l*2,self.h*2,"roof.csv")
            buildroof(self.x+13,self.y+self.h,self.z+13,self.w*2,self.l*2,self.h,"roof.csv")         
house1=House(100,100,100,10,10,10)
house2=House(100,100,113,10,10,10)
house3=House(100,100,126,10,10,10)
house4=House(113,100,100,10,10,10)
house5=House(113,100,113,10,10,10)
house6=House(113,100,126,10,10,10)
house7=House(126,100,100,10,10,10)
house8=House(126,100,113,10,10,10)
house9=House(126,100,126,10,10,10)
houses=[]
houses.append(house1)
houses.append(house2)
houses.append(house3)
houses.append(house4)
houses.append(house5)
houses.append(house6)
houses.append(house7)
houses.append(house8)
houses.append(house9)
house1.buildbuild()
house2.buildbuild()
house3.buildbuild()
house4.buildbuild()
house5.buildbuild()
house6.buildbuild()
house7.buildbuild()
house8.buildbuild()
house9.buildbuild()
house1.buildhall()
house1.buildwall()
houses.ishouse()



