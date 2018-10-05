#爬一个图片编号有规律的图集

import requests
import time
#from bs4 import BeautifulSoup
#url = 'http://img.mmjpg.com/2017/1075/1.jpg'
urlList = []
def createUrl():
	for i in range(1,40):
		url = 'https://ii.hywly.com/a/1/4500/'+str(i)+'.jpg'
		urlList.append(url)
	print(urlList)
	return urlList


def getpic(urllist):
	headers = {
		'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) ' 'Chrome/65.0.3325.181 Safari/537.36',
		'Referer': "http://www.meituri.com"}
	num =1
	for i in urlList:
		r = requests.get(i,headers=headers).content
		time.sleep(2)
		with open('D:\images\%d.jpg'%num,'wb') as f:
			f.write(r)
			f.close()
		num += 1

getpic(createUrl())
#createUrl()