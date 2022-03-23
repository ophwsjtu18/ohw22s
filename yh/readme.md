# Bonjour tout le monde
bonjour!!!\
c'est moi!\
![rararara](https://github.com/ophwsjtu18/ohw22s/blob/main/OIP-C.jpg)

# Mon premier devoir---grand bâtiment de TNT!!
c'est son démonstration
![](https://github.com/ophwsjtu18/ohw22s/blob/main/yh/images/2022-03-23_21.30.46.png)
Et suivant sont les codes Python
```# define a new function, that builds a house 3*3
def house():
    # Calculate the midpoints of the front face of the house  
    midx = x+SIZE/2
    midy = y+SIZE/2

    # Build the outer shell of the house
    mc.setBlocks(x, y, z, x+SIZE, y+SIZE, z+SIZE, block.COBBLESTONE.id)
    
    # Carve the insides out with AIR      
    mc.setBlocks(x+1, y, z+1, x+SIZE-2, y+SIZE-1, z+SIZE-2, block.AIR.id)

    # Carve out a space for the doorway
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)

    # Carve out the left hand window
    mc.setBlocks(x+3, y+SIZE-3, z, midx-3, midy+3, z, block.GLASS.id)
    
    # Carve out the right hand window     
    mc.setBlocks(midx+3, y+SIZE-3, z, x+SIZE-3, midy+3, z, block.GLASS.id)

    # Add a wooden roof 
    mc.setBlocks(x, y+SIZE, z, x+SIZE, y+SIZE, z+SIZE, block.WOOD.id)
    
    # Add a woolen carpet, the colour is 14, which is red.
    mc.setBlocks(x+1, y-1, z+1, x+SIZE-2, y-1, z+SIZE-2, block.WOOL.id, 14)
  
# Get the players position    
pos = mc.player.getTilePos()

# Decide where to start building the house, slightly away from player
x = pos.x + 2
y = pos.y
z = pos.z
  
# build 5 houses, for a whole street of houses
for h in range(5):
    # build one house
    house()
    # move x by the size of the house just built
    x = x + SIZE
    
# END
