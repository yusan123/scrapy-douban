import requests
try:
    import cookielib
except:
    import http.cookiejar as cookielib
import re


agent="Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:63.0) Gecko/20100101 Firefox/63.0"
header={
    "HOST":"www.zhihu.com",
    "Referer":"https://www.zhihu.com",
    "User-Agent":agent
}


def get_xsrf():
    #resp = requests.get("https://www.zhihu.com",headers=header)
    #print(resp.text)

    text='<input type="hidden" name="_xsrf" value="ahjdfhjkjashdjk1jhj878" />'
    res = re.findall(r'.*name="_xsrf" value="(.*?)"',text)
    if res:
        print(res.group(1))

def zhihu_login(account,passward):
    #知乎登录的方法
    if re.match(r'^1\d{10}',account):
        print("使用手机号登录")


    pass

get_xsrf()