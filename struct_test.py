"""
数据打包
"""

import struct

# 1 lily  18  1.65 
fmt = "i4sif"

# st = struct.Struct(fmt)
#
# data = st.pack(1,b"Baron",18,1.65)
# print(data)
#
# data = st.unpack(data)
# print(data)

data = struct.pack(fmt,1,b"Lucy",18,1.66)
print(data)

data = struct.unpack(fmt,data)
print(data)