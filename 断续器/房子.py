Python 3.10.2 (tags/v3.10.2:a58ebcc, Jan 17 2022, 14:12:15) [MSC v.1929 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
import mcpi.minecraft as minecraft
将 mcpi.block 导入为块
mc = 我的世界。Minecraft.create（）
pos = mc.player.getTilePos（）
对于 a 在范围内（10）：
对于 b 在范围（10）：
对于 c 在范围（8）：
对于 d 在范围（3）：
mc.setBlock（pos.x+a+20*d， pos.y+b， pos.z+c， block.TNT.id）
对于 a 在范围（8）：
对于 b 在范围（8）：
对于 c 在范围（6）：
对于 d 在范围（3）：
mc.setBlock（pos.x+a+20*d+1， pos.y+b+1， pos.z+c+1， block.AIR.id）
对于 a 在范围内（4）：
对于 b 在范围（4）：
对于 c 在范围（1）：
对于 d 在范围（3）：
mc.setBlock（pos.x+a+20*d+3， pos.y+b+1， pos.z+c， block.AIR.id）