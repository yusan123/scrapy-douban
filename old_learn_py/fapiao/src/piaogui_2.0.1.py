#encoding = 'utf-8'
'''
@by yusen
@2017/9/17
v1.0

'''
import wx
import sqlite3
import time
from PIL import Image


con = sqlite3.connect('fapiao.db') #链接到数据库
cur = con.cursor() #获取游标


def prtres(): #定义打印函数
  
    tplt = "{:5}\t{:10}\t{:6}\t{:10}\t{:50}"
    res = tplt.format("票号","开票日期","经办人","金额","用途")+'\n'
    rows = cur.fetchall()
    for row in rows:
        res+=tplt.format(row[0],row[1],row[2],row[3],row[4])+'\n'
    
    ret = (str(res))
    return ret

        
def checkbyid(event):	#定义通过id查询的事件
    if idbox.GetValue()=='*':# 输入*号显示所有数据
        cur.execute('select * from piao')
    elif idbox.GetValue()=='':#解决模糊查询时不输入内容也显示所有数据
        pass
    else:
    	#id模糊查询
        cur.execute('select * from piao where id glob ?',('*'+idbox.GetValue()+'*',))
    contents.SetValue(prtres())
    
# def checkbydate(event): #定义通过日期查询的事件
#     cur.execute('select * from piao where date glob ?',('*'+datebox.GetValue()+'*',))
#     contents.SetValue(prtres())
    
def checkbyjbr(event): #定义通过经办人查询的事件
    if jbrbox.GetValue()=='':#解决模糊查询时不输入内容也显示所有数据
        pass
    else:
        cur.execute('select * from piao where jbrname glob ?',('*'+jbrbox.GetValue()+'*',))
    contents.SetValue(prtres())

def chkbydateandjbr(event):
	#当日期输入框和经办人输入框都不为空时，执行多条件查询
    if (len(datebox.GetValue())!=0) and (len(jbrbox.GetValue())!=0): 
        cur.execute('select * from piao where date glob ? and jbrname glob ?',('*'+datebox.GetValue()+'*','*'+jbrbox.GetValue()+'*',))
    else:
        if datebox.GetValue()!='':#只有当不为空时执行模糊查询，也是解决模糊查询时，不输入内容打印所有信息
            cur.execute('select * from piao where date glob ?',('*'+datebox.GetValue()+'*',))
    contents.SetValue(prtres())  
def showpic(event): #定义显示图片的事件
	try:
		img = Image.open('./img/'+imgbox.GetValue()+'.jpg')
		img.show()
	except:
		#wx.MessageBox(None,'编号为%s的图片不存在'%str(prtres()[1]))
		wx.MessageBox('该图片不存在','提示')

app =  wx.App()
win = wx.Frame(None,title = '发票管理v1.5 2017924(多条件和模糊查询)',size = (520,675))

idbtn = wx.Button(win,label = '按票号查询',pos = (360,5),size = (140,25))
idbox = wx.TextCtrl(win,pos = (5,5),size = (350,25))

datebtn = wx.Button(win,label = '按日期查询',pos = (360,35),size = (140,25))
datebox = wx.TextCtrl(win,pos = (5,35),size = (350,25))

jbrbtn = wx.Button(win,label = '按经办人查询',pos = (360,65),size = (140,25))
jbrbox = wx.TextCtrl(win,pos = (5,65),size = (350,25))

imgbtn = wx.Button(win,label = '显示图片',pos=(360,600),size=(140,25))
imgbox = wx.TextCtrl(win,pos = (5,600),size = (350,25))

contents = wx.TextCtrl(win,pos = (5,95),size = (495,500),style = wx.TE_MULTILINE or wx.HSCROLL)

#为每个按钮绑定事件
idbtn.Bind(wx.EVT_BUTTON,checkbyid)
#
datebtn.Bind(wx.EVT_BUTTON,chkbydateandjbr)
#
#     datebtn.Bind(wx.EVT_BUTTON,checkbydate) #不需要单独的日期查询函数
jbrbtn.Bind(wx.EVT_BUTTON,checkbyjbr)
imgbtn.Bind(wx.EVT_BUTTON,showpic)


win.Show()
app.MainLoop()
