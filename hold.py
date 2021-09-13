"""
空洞文件 GIT添加无用备注
"""

f = open('test','wb')

f.write(b'')

f.seek(1024) #　命令行查看文件大小，从结尾向后移动１M

f.write(b'b')

f.close()

