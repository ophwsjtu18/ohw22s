# Import necessary modules
import mcpi.minecraft as minecraft
import mcpi.block as block

# Connect to Minecraft
mc = minecraft.Minecraft.create()

def house(x,y,z,l,w,h,m):
    # Calculate the midpoints of the front face of the house
    midx = x+w/2
    midy = y+l/2  
    
    # Build the outer shell of the house
    mc.setBlocks(x, y, z, x+w, y+l, z+h, m)
    
    # Carve the insides out with AIR    
    mc.setBlocks(x+1, y, z+1, x+w-2, y+l-1, z+h-2, block.AIR.id)

    # Carve out a space for the doorway
    mc.setBlocks(midx-1, y, z, midx+1, y+3, z, block.AIR.id)

    # Carve out the left hand window
    mc.setBlocks(x+3, y+l-3, z, midx-3, midy+3, z, block.GLASS.id)
    
    # Carve out the right hand window    
    mc.setBlocks(midx+3, y+l-3, z, x+w-3, midy+3, z, block.GLASS.id)

    # Add a wooden roof  
    mc.setBlocks(x, y+l, z, x+w, y+l, z+h, block.WOOD.id)

    # Add a woolen carpet, the colour is 14, which is red.
    mc.setBlocks(x+1, y-1, z+1, x+w-2, y-1, z+h-2, block.WOOL.id, 14)
    

# Get the players position
pos = mc.player.getPos()

# Decide where to start building the house, slightly away from player
x = pos.x + 2
y = pos.y
z = pos.z

length = 10
width = 10
height = 8
material = block.COBBLESTONE.id
# run the house() function that was defined by def house():
# this will build a house at x,y,z
for i in range(3):
    for j in range(3):
        house(x + length * i * 2, y, z + width * j + 5, length, width, height, material)


# END