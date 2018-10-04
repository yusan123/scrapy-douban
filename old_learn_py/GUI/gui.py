import wx

def load(event):
    file = open(filename.GetValue())
    contents.SetValue(file.read())
    file.close()

def save(event):
    file = open(filename.GetValue(),'w')
    file.write(contents.GetValue())
    file.close()
app =  wx.App()

win = wx.Frame(None,title = '哈哈',size = (410,335))

loadbtn = wx.Button(win,label = 'Open',pos = (225,5),size = (80,25))
savebtn = wx.Button(win,label = 'Save',pos = (315,5),size = (80,25))
filename = wx.TextCtrl(win,pos = (5,5),size = (210,25))
contents = wx.TextCtrl(win,pos = (5,35),size = (390,260),style = wx.TE_MULTILINE or wx.HSCROLL)

loadbtn.Bind(wx.EVT_BUTTON,load)
savebtn.Bind(wx.EVT_BUTTON,save)
win.Show()

app.MainLoop()
