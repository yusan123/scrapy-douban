import requests
from bs4 import BeautifulSoup
import re


def getHtmlText(url): #获取页面信息
	kv = {'user-agent':'Mozilla/5.0'}
	r = requests.get(url,headers = kv)
	r.encoding = 'utf-8'
	return r.text

def makeUrl(): #构造包含250部影片的10个网页
	urlList = []
	for i in range(0,250,25):
		url ='https://movie.douban.com/top250?start=%s&filter='%str(i)
		urlList.append(url)
	#print(urlList)
	return urlList

def parserHtml(urlList):
	infoDic = {} #存储所有影片信息的字典格式如：{1:{'序号':'1','名字':'abc','日期':'1999','评分':'9.0'},2:{},3:{}}
	num =1
	for url in urlList:
		soup = BeautifulSoup(getHtmlText(url),'html.parser')
		x =soup("div","info") #每一部电影的所有信息都存在一个class=info 的div标签下，x代表了每一页25部影片的信息
		for i in x:	
			filmDic = {}	#存储每一部影片的字典格式如 {'序号':'1','名字':'abc','日期':'1999','评分':'9.0'}
			
			#本来想加上电影类型，国家，导演，主演，弄不出来
			filmDic['序号']=str(num)
			filmDic['名称']=i('span','title')[0].string
			filmDic['上映时间']=re.findall(r'[\d]{4}',str(i('p')))[0]
			filmDic['豆瓣评分']=i('span','rating_num')[0].string
			filmDic['豆瓣链接']=i('a')[0]['href']
			infoDic[num]=filmDic
			num+=1
	#print(infoDic[250])
	return infoDic
def prtandtxtlist(dic):
	geshi = '{:1}\t{:10}\t{:4}\t{:2}\t{:28}\t'
	print(geshi.format("序号","名称","上映时间","豆瓣评分","豆瓣链接"))
	for i in range(1,251):
		print(geshi.format(i,dic[i]['名称'],dic[i]["上映时间"],dic[i]["豆瓣评分"],dic[i]["豆瓣链接"]))
	

	with open('doubantop250.txt','w') as f:
		f.write(geshi.format("序号","名称","上映时间","豆瓣评分","豆瓣链接")+'\n')
		for i in range(1,251):
			f.write(geshi.format(i,dic[i]['名称'],dic[i]["上映时间"],dic[i]["豆瓣评分"],dic[i]["豆瓣链接"])+'\n')
		f.close()


def main():
	prtandtxtlist(parserHtml(makeUrl()))

main()
x= input()







