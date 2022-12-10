#*-encoding=utf-8-*
import os

print('upload')

# os.mkdir('director')
# os.rmdir('directo')#os.mkdir创建文件，os.rmdir删除文件夹
def createNewTextFile():
    num=10#定义文件数量
    dir_path = "C:\\Users\\jackl\\PycharmProjects\\github_newProject\\director\\"#选择文件路径，双引号隔开
    for i in range(1,num+1):
        with open(dir_path + '第' + str(i) + '个文件' + '.txt', 'w') as f:
            f.write(str(i * i))#写文件内容
createNewTextFile()