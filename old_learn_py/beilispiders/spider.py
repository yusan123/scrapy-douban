#爬一个图片编号有规律的图集

import requests
import time
#from bs4 import BeautifulSoup
#url = 'http://img.mmjpg.com/2017/1075/1.jpg'
urlList = []
def createUrl():
	for i in range(1,50):
		url = 'http://img1.mm131.com/pic/3081/'+str(i)+'.jpg'
		urlList.append(url)
	print(urlList)
	return urlList


def getpic(urllist):
	num =1
	for i in urlList:
		r = requests.get(i).content
		time.sleep(0.5)
		with open('E:\images\%d.jpg'%num,'wb') as f:
			f.write(r)
			f.close()
		num += 1

getpic(createUrl())
#createUrl()