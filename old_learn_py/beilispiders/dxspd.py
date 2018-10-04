#coding:uft-8

#定向爬取大学排名
import requests
from bs4 import BeautifulSoup
import bs4

def getText(url):
	try:
		r = requests.get(url)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ''
		print('shibai')


def getInfoList(ulist,html):
	soup = BeautifulSoup(html,'html.parser')
	for tr in soup.find('tbody').children:
		if isinstance(tr,bs4.element.Tag):
			tds = tr('td')
			ulist.append([tds[0].string,tds[1].string,tds[2].string,tds[3].string])

def prtInfoList(ulist,num):
	print("{:^10}\t{:^6}\t{:^10}\t{:^10}".format('排名','大学名称','地区','得分'))
	for i in range(num):
		u = ulist[i]
		print("{:^10}\t{:^6}\t{:^10}\t{:^10}".format(i+1,u[1],u[2],u[3]))


def main():
	uinfo = []
	url = 'http://www.zuihaodaxue.cn/zuihaodaxuepaiming2017.html'
	html = getText(url)
	getInfoList(uinfo,html)
	prtInfoList(uinfo,30)

main()