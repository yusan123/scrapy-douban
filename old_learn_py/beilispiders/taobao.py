# https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170815&ie=utf8
# https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170815&ie=utf8&p4ppushleft=5%2C48&s=48
# https://s.taobao.com/search?q=%E6%89%8B%E6%9C%BA&imgfile=&js=1&stats_click=search_radio_all%3A1&initiative_id=staobaoz_20170815&ie=utf8&p4ppushleft=5%2C48&s=96
import re
import requests
import time
def getText(url):
	try:
		kv = {"user-agent":"Mozilla/5.0"}
		r = requests.get(url,timeout = 30,headers = kv)
		r.raise_for_status()
		r.encoding = r.apparent_encoding
		return r.text
	except:
		return ''



def paserPage(ils,html):
	titleList = re.findall(r'\"raw_title\"\:\".*?\"',html)
	priceList = re.findall(r'\"view_price\"\:\".*?\"',html)
	salesList = re.findall(r'\"view_sales\"\:\".*?\"',html)
	for i in range(len(titleList)):
		title = eval(titleList[i].split(':')[1])
		price = eval(priceList[i].split(':')[1])
		sale = eval(salesList[i].split(':')[1])
		ils.append([price,title,sale])

def prtInfo(ils):
	tplt = "{:3}\t{:3}\t{:24}\t{:5}"
	print(tplt.format("编号","价格","商品名","售出"))
	count = 1
	for i in ils:
		print(tplt.format(count,i[0],i[1],i[2]))
		count += 1

def saveInfo(ils):
	tplt = "{:3}\t{:3}\t{:24}\t{:5}"
	count = 1
	with open('%s.txt'%goods,'w') as f:
		f.write(tplt.format("编号","价格","商品名","售出") +'\n')
		for i in ils:
			f.write(tplt.format(count,i[0],i[1],i[2]) +'\n')
			count += 1
		f.close()

def main():
	global goods
	try:
		goods = input('请输入你要在淘宝网上搜索的物品名称：')
		pageNum = int(input('请输入要爬取的页数(每页有44条)：'))
		startUrl = 'https://s.taobao.com/search?q=' + goods
		infoLs = []
		for i in range(pageNum):
				url = startUrl + '&s=' + str(i*44)
				html = getText(url)
				paserPage(infoLs,html)
				time.sleep(2)
		print('成功获取%d条数据'%(44*pageNum))
		prtInfo(infoLs)
		saveInfo(infoLs)
		print('已将数据写入当前目录下<<%s>>文件'%(goods +'.txt'))
	except:
		print('获取失败，请重试！')
main()
x = input()