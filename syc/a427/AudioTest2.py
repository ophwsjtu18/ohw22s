import os
from chardet import *

website='https://cn.bing.com/search?q='+ +'&form=QBLH&sp=-1&pq='+ +'&sc=8-3&qs=n&sk=&cvid=9599980DDE5444178FF8AB662D0EB7F5'
os.system("\"C:/Program Files/Internet Explorer/iexplore.exe\" %s"%website)

# s=["麻婆豆腐"]
# b=str(s[0].encode('utf-8'))
# b=b[2:-1]
# string=b.replace('\\x','%')
# print(string)