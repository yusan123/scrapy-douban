import re
s = 'dsdfsdank11img src="http://img.mmjpg.com/small/2017/1066.jpgfhttp://img.mmjpg.com/small/2017/1072.jpgsdfsdadfgfjpg.commjpg.com/sma'
pat = r'http://.+?\.jpg'
res = re.findall(pat,s)
print(res)
print(len(res))
