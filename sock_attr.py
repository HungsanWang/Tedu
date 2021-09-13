"""
套接字属性介绍
"""
from socket import *

# 创建套接字
s = socket()

# 设置端口可以立即重用，绑定地址之前
s.setsockopt(SOL_SOCKET,SO_REUSEADDR,1)


s.bind(('127.0.0.1',8989))
s.listen(3)
c,addr = s.accept()


c.recv(1024) #　提供阻塞
