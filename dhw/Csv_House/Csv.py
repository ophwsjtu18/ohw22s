
import mcpi.minecraft as minecraft
import mcpi.block as block
import time

mc = minecraft.Minecraft.create()
pos = mc.player.getTilePos()


def house(x,y,z,h,w,l,m,roofname):
   
   for b in range(w):
         for c in range(l):
              mc.setBlock(x+b, y, z+c,m)
 
   for a in range(h):
     for b in range(l):
        mc.setBlock(x+b,y+a, z,m)
        mc.setBlock(x+b,y+a, z+w-1, m)
    
   for a in range(h):
     for b in range(w):
        mc.setBlock(x,y+a, z+b,m)
        mc.setBlock(x+l-1,y+a, z+b,m)    
    
   for a in range(2):
      for b in range(2): 
            mc.setBlock(x,b+y+2, z+a+4, m)
   
   for a in range(w):
      for b  in range(l):
            mc.setBlock(x+a,y+h-1, z+b,m)
   mc.setBlock(x+5, y+1,z,0)
   mc.setBlock(x+5, y+2, z,0)
   mc.setBlock(x+5, y+3,z,0)
   mc.setBlock(x+4, y+1, z,0)
   mc.setBlock(x+4, y+3,z,0)
   mc.setBlock(x+4, y+2, z,0)


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
   print(roof[3][4])

   for i in range(10):
     for j in range(10):
        if roof[i][j]==0:
           #print("I will setBlock with mud")
            mc.setBlock(x+i,y+h,z+j,2)
        else:
            #print("I will setBlock with ...")
            mc.setBlock(x+i,y+h,z+j,3)

   f.close()

for a in range (0,3):
    for b in range (0,3):
      house (271+15*a,56,200+15*b,10,10,10,1,"C:/Users/DHW/Desktop/KaiYuanChuangKeShiJian/KaiYuan220420/roof.csv")

while True:
  pos1 = mc.player.getTilePos()
  mc.postToChat(f"x:{pos1.x}")
  time.sleep(0.5)
  mc.postToChat(f"y:{pos1.y}")
  time.sleep(0.5)
  mc.postToChat(f"z:{pos1.z}")
  time.sleep(0.5)
  print("time_")
  
  for a in range (0,3):
    for b in range (0,3):
        if pos1.x>=271+15*a and pos1.x<=271+15*a+10 and pos1.y>=56 and pos1.y<=56+10 and pos1.z>=200+15*a and pos1.z<=200+15*a+10:
           mc.postToChat("welcome home")
       






