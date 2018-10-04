import requests
from bs4 import BeautifulSoup
import lxml
import os
import re
import time


def getHtmlText(url): #获取页面信息
	kv = {'user-agent':'Mozilla/5.0'}
	r = requests.get(url,headers = kv)
	r.encoding = 'GB2312'
	return r.text

	#获取主页链接的列表格式[['一组图片链接名字','http://wwwxxx.html']]
def getUrlList(x): 
	ddlist = []
	#tagList = []
	#一代的写法
	#soup = BeautifulSoup(x,'lxml')
	# for tag in soup('dd')[1:]: #dd标签的第一个不是图片
	# 	ddlist.append([tag.string,(tag.contents[0]['href'])])
	#*********************直接用正则全部匹配***********************
	shuzi = 0
	for i in re.findall(r'http://www\.mm131\.com/.+/[0-9]{4}\.html">[^<img].+</a>',x):
		x = i.find('html">')
		#print(str(shuzi)+i+'\n')
		ddlist.append([i[x+6:-4],i[:x+4]])
		shuzi+=1

	# xlist = set(ddlist) #去重复
	# ddlist=list(xlist)
	# for i in ddlist:
	# 	print(i[0]+'\n')
	print('获取到%d组图片'%len(ddlist))
	return ddlist


	#利用正则找到每组图片的数量
	#用bs把一组图片的url构造成列表
def makePicUrlList(list):
	url = list[1] 
	#print(url)
	piclist = [] #生成存放图片链接的空列表
	#从一组图片的链接页面中找到对应图片的编号（是一个四位数的数）
	pagecode = url[-9:-5] 
	#调用getHtmlText()获取页面并用bs4解析
	soup = BeautifulSoup(getHtmlText(url),'lxml')
	#用re获得每组图片的数量
	picnum = int(soup(string = re.compile(r'共\d*页'))[0][1:-1])
	#具体构造每一张图片的链接并存入对应的列表
	for num in range(picnum):
		#链接地址为'http://img1.mm131.com/pic/2301/1.jpg'从1开始
		picurl ='http://img1.mm131.com/pic/'+pagecode+'/'+str(num+1)+'.jpg'
		num+=1
		piclist.append(picurl)#存入列表
	#print(piclist)
	return piclist


def getPic(list,piclist):
	tag =list[1][21:-10]
	picnum = len(piclist)
	xuhao = ddlist.index(list)
	dirname = 'E:\pic\%s'%(str(xuhao)+'['+tag+']'+'['+str(picnum)+'P]'+list[0]+(str(int(time.time())-startTime))) #构造每组图片的目录名
	os.mkdir(dirname) #创建目录
	os.chdir(dirname) #切到目录
	count = 1
	print('第%d组开始下载<<%s>>——总共%d张存入E:\pic'%(xuhao,list[0],picnum))
	#print(count)
	for pic in piclist:#遍历每组图片的列表将其写入目录
		try:
			r = requests.get(pic,headers={'user-agent':'Mozilla/5.0'}).content
			time.sleep(0.02)
			with open((dirname+'\\'+list[0][:8]+str(count)+'.jpg'),'wb') as f:
				f.write(r)
				f.close()
			print('\r正在下载第%d/%d张'%(count,picnum),end='')
			count += 1
		except:
			continue
		
	print('\n第%d组下载<<%s>>完毕——总共%d张存入E:\pic'%(xuhao,list[0],picnum))

def main():
	global startTime
	startTime  = int(time.time())
	indexUrl = 'http://www.mm131.com/'
	path = r'E:\pic' 
	if not os.path.exists(path): #如果主目录不存在，则创建
		os.mkdir(path)
	global ddlist
	ddlist = getUrlList(getHtmlText(indexUrl)) #获取主页上的链接
	for group in ddlist:
		#调用下载图片
		getPic(group,makePicUrlList(group))
		time.sleep(0.2)
	print('下载完毕，总共下载了%d组图片'%(len(ddlist)))


main() #主函数运行
x = input()


