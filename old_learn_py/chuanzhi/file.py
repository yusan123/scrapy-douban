#coding=utf-8
import os 

#dirPath = r'C:\Users\yousan\Desktop\new'
def getNewName(name='新建文件'):
	name = input('请输入文件的新名字（默认为*新建文件*）：')
	return name
def getNum(num=20):
	num = int(input('请输入目录下新建文件的数量（默认为20个）：'))
	return num
def getPath():
	try:
		path = input('请输入文件目录所在的路径（默认D:\\new盘根目录）：')
		os.chdir(path)
	except:
		path = 'D:\\new\\'
	return path

#在指定目录下创建指定输了文件
def createNewfile(num,Path):
	try:
		os.chdir(Path)
	except:
		os.mkdir(Path)
	finally:
		os.chdir(Path)
		for i in range(1,num+1):
			fileName = str(i) + '.txt'
			f = open(fileName,'w')
			f.write('李 娟 老 婆 是个大笨猪')
			f.close()

#批量修改文件名
def chAllFileName(newName,path,firstnum):
	os.chdir(path)
	fileNameList = os.listdir(path)
	for i in fileNameList:
		os.rename(i,newName+str(firstnum)+'.txt')
		firstnum+=1


def main():
	newName  = getNewName()
	path = getPath()
	num = getNum()
	try:
		chAllFileName(newName,path,1)
	except:
		createNewfile(num,path)
		chAllFileName(newName,path,1)
	print('修改成功')
main()
x = input()
