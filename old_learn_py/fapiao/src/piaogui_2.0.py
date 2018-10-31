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


con = sqlite3.connect('fapiao.db')
cur = con.cursor()


def prtres():
  
    tplt = "{:15}\t{:15}\t{:15}\t{:15}\t{:50}"
    res = tplt.format("票号","开票日期","经办人","金额","用途")+'\n'
    rows = cur.fetchall()
    for row in rows:
        res+=tplt.format(row[0],row[1],row[2],row[3],row[4])+'\n'
    return str(res)

        
def checkbyid(event):
    if idbox.GetValue()=='*':
        cur.execute('select * from piao')
    else:
        cur.execute('select * from piao where id glob ?',('*'+idbox.GetValue()+'*',))
    contents.SetValue(prtres())
    
def checkbydate(event):
    cur.execute('select * from piao where date glob ?',('*'+idbox.GetValue()+'*',))
    contents.SetValue(prtres())
    
def checkbyjbr(event):
    cur.execute('select * from piao where jbrname glob ?',('*'+idbox.GetValue()+'*',))
    contents.SetValue(prtres())

def showpic(event): #定义显示图片的事件
	try:
		img = Image.open('./img/'+idbox.GetValue()+'.jpg')
		img.show()
	except:
		#wx.MessageBox(None,'编号为%s的图片不存在'%str(prtres()[1]))
		wx.MessageBox('该图片不存在','提示')

app =  wx.App()
win = wx.Frame(None,title = '发票管理v2.0 2017923',size = (800,700))
bkg = wx.Panel(win)


#idbtn = wx.Button(win,label = '按票号查询',pos = (425,5),size = (140,25))
# idbox = wx.TextCtrl(win,pos = (5,5),size = (400,25))
# datebtn = wx.Button(win,label = '按日期查询',pos = (425,35),size = (140,25))
# datebox = wx.TextCtrl(win,pos = (5,35),size = (400,25))
# jbrbtn = wx.Button(win,label = '按经办人查询',pos = (425,65),size = (140,25))
# jbrbox = wx.TextCtrl(win,pos = (5,65),size = (400,25))
# imgbtn = wx.Button(win,label = '显示图片',pos=(425,715),size=(140,35))
# imgbox = wx.TextCtrl(win,pos = (5,715),size = (400,35))


idbtn = wx.Button(bkg,label = '按票号查询')
idbtn.Bind(wx.EVT_BUTTON,checkbyid)

datebtn = wx.Button(bkg,label = '按日期查询')
datebtn.Bind(wx.EVT_BUTTON,checkbydate)

jbrbtn = wx.Button(bkg,label = '按经办人查询')
jbrbtn.Bind(wx.EVT_BUTTON,checkbyjbr)

imgbtn = wx.Button(bkg,label = '显示图片')
imgbtn.Bind(wx.EVT_BUTTON,showpic)

idbox = wx.TextCtrl(bkg)
# datebox = wx.TextCtrl(bkg)
# jbrbox = wx.TextCtrl(bkg)
# imgbox = wx.TextCtrl(bkg)

contents = wx.TextCtrl(bkg,style = wx.TE_MULTILINE | wx.HSCROLL)

hbox = wx.BoxSizer()
hbox.Add(idbox,proportion=1,flag=wx.EXPAND)
# hbox.Add(datebox,proportion=1,flag=wx.EXPAND)
# hbox.Add(jbrbox,proportion=1,flag=wx.EXPAND)
# hbox.Add(imgbox,proportion=1,flag=wx.EXPAND)
hbox.Add(idbtn,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(datebtn,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(jbrbtn,proportion=0,flag=wx.LEFT,border=5)
hbox.Add(imgbtn,proportion=0,flag=wx.LEFT,border=5)

vbox = wx.BoxSizer(wx.VERTICAL)
vbox.Add(hbox,proportion=0,flag=wx.EXPAND | wx.ALL,border=5)
vbox.Add(contents,proportion=1,flag=wx.EXPAND | wx.LEFT | wx.BOTTOM | wx.RIGHT,border=5)

bkg.SetSizer(vbox)
win.Show()
app.MainLoop()
