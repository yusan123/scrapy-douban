import requests
from bs4 import BeautifulSoup
import lxml
import os
import re
import time


def getHtmlText(url): #获取页面信息
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/65.0.3325.181 Safari/537.36',
		'Referer': "https://www.meituri.com"}
	r = requests.get(url,headers = headers)
	r.encoding = 'utf-8'
	# print(r.text)
	return r.text



	#使用xpath重新解析
def getUrlList(html):
	ddlist = []
	tree = lxml.etree.HTML(html)
	list =tree.xpath("//div[@class='hezi']//li")
	for li in list:
		url = li.xpath("./a/img/@src")[0]
		picNum = li.xpath(".//span[@class='shuliang']//text()")[0]
		tags = "-".join(li.xpath(".//p[3]//a//text()"))
		modelName = li.xpath(".//p[2]/a//text()")
		print(modelName)
		ddlist.append([picNum+tags,url])
	print('获取到%d组图片'%len(ddlist))
	print(ddlist)
	return ddlist


	#用bs把一组图片的url构造成列表
def makePicUrlList(list):
	url = list[1] 
	print(url)
	piclist = [] #生成存放图片链接的空列表

	picnum = int(list[0][:list[0].index("P")])
	#具体构造每一张图片的链接并存入对应的列表
	for num in range(picnum):
		#链接地址为'https://ii.hywly.com/a/1/19322/0.jpg'从1开始
		picurl = url[:-5] +str(num)+'.jpg'
		piclist.append(picurl)#存入列表
	print(piclist)
	return piclist


	# list 是每一个ddlist[[]] 中的一个[title,url] piclist是组合生成的[]
def getPic(list,piclist):
	picnum = len(piclist)
	xuhao = ddlist.index(list)
	# dirname = 'D:\pic\%s'%(str(xuhao)+'['+tag+']'+'['+str(picnum)+'P]'+list[0]+(str(int(time.time())-startTime))) #构造每组图片的目录名
	dirname = 'D:\pic\%s'%(str(xuhao)+list[0]+(str(int(time.time())-startTime))) #构造每组图片的目录名
	os.mkdir(dirname) #创建目录
	os.chdir(dirname) #切到目录
	count = 1
	print('第%d组开始下载<<%s>>——总共%d张存入E:\pic'%(xuhao,list[0],picnum))
	#print(count)
	for pic in piclist:#遍历每组图片的列表将其写入目录
		try:
			headers = {
				'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/65.0.3325.181 Safari/537.36',
				'Referer': "http://www.meituri.com"}
			r = requests.get(pic,headers=headers).content
			time.sleep(0.02)
			with open((dirname+'\\'+list[0][:8]+str(count)+'.jpg'),'wb') as f:
				f.write(r)
				f.close()
			print('\r正在下载第%d/%d张'%(count,picnum),end='')
			count += 1
		except:
			continue
		
	print('\n第%d组下载<<%s>>完毕——总共%d张存入D:\pic'%(xuhao,list[0],picnum))

def main():
	global startTime
	startTime  = int(time.time())
	indexUrl = 'https://www.meituri.com/zhongguo'
	path = r'D:\pic'
	if not os.path.exists(path): #如果主目录不存在，则创建
		os.mkdir(path)
	global ddlist
	ddlist = getUrlList(getHtmlText(indexUrl)) #获取主页上的链接
	for group in ddlist:
		#调用下载图片
		getPic(group,makePicUrlList(group))
		time.sleep(0.5)
	print('下载完毕，总共下载了%d组图片'%(len(ddlist)))


main() #主函数运行
# getUrlList(getHtmlText("https://www.meituri.com"))
x = input()


