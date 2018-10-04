#爬一个网页上的所有jpg图片
import requests
import re
import time
url = 'http://699pic.com/tupian/yuangongzhijia.html?sourcefrom=2'
r = requests.get(url)

def geturl():
	pat = r'http://.+?\.jpg'
	urlList = list(set(re.findall(pat,r.text)))
	print(urlList)
	print(len(urlList))
	return urlList

def getpic(urlList):
	zongshu = len(urlList)
	num = 1
	for i in urlList:
		r = requests.get(i)
		time.sleep(0.2)
		with open('./pic/%d.jpg'%num,'wb') as f:
		 	f.write(r.content)
		 	f.close()
		print('正在下载%d/%d张图片'%(num,zongshu))
		num += 1
print(r.status_code)
#print(r.request.headers)
# with open('./1.jpg','wb') as f:
# 	f.write(r.content)
getpic(geturl())