import sqlite3
import time

con = sqlite3.connect('fapiao.db')
cur = con.cursor()
left = ' '*8


def get_mingli():	#获取用户输入的指令
	try:
		mingling = int(input('请输入你需要的功能代码：'))
		print('********************************')
		return mingling
	except:
		pass

def prt_menu():  #定义打印主界面菜单函数
	print('欢迎使用发票信息查询系统')
	time.sleep(1)
	print("-"*30),
	#print('anthor: yu    date:20170808')
	print("-"*30),
	print(left+'选项 项目')
	print(left+'1.通过编号查询')
	print(left+'2.通过日期查询')
	print(left+'3.通过经办人查询')
	print(left+'4.退出本系统')
	print('~'*30),
	print('~'*30)

def prtres():
	tplt = "{:10}\t{:10}\t{:6}\t{:10}\t{:30}"
	print(tplt.format("票号","开票日期","经办人","金额","用途"))
	rows = cur.fetchall()
	for row in rows:
		print(tplt.format(row[0],row[1],row[2],row[3],row[4]))


def getord():
	order = int(input('请输入你需要的功能代码（数字）：'))
	return order

def checkbyid():
	id_ = input('请输入编号：')
	cur.execute('select * from piao where id = ?',(id_,))
	prtres()

def checkbydate():
	date = input('请输入日期（yyyy/mm/dd)：')
	cur.execute('select * from piao where date = ?',(date,))
	prtres()
	
def checkbycont():
	jbrname = input('请输入经办人姓名：')
	cur.execute('select * from piao where jbrname = ?',(jbrname,))
	prtres()


def main():
	while True:
		print('\n'*10),
		prt_menu()
		mingling=get_mingli()
		if mingling==1:#
			checkbyid()
		elif mingling==2:#
			checkbydate()
		elif mingling==3:#
			checkbycont()	
		elif mingling==4:
			print('感谢您使用本系统，欢迎您再次使用')
			time.sleep(0)
			break
		else:
			print('您输入的命令有误，请重新输入！！！')

if __name__ == '__main__':
	main()