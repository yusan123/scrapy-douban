#coding:utf-8
import time 
txl=[ 	{'name':'李j','num':'18789456623'},
		{'name':'yeeen','num':'18791220794'},
		{'name':'张三','num':'18792322794'}
		]
nameList = []
def get_namelist():
	global nameList
	nameList = []
	for i in txl:
		nameList.append(i['name'])

# def clearpingmu():
# 	print('/n'*50)
left = ' '*8
def get_mingli():	#获取用户输入的指令
	try:
		mingling = int(input('请输入你需要的功能代码：'))
		print('********************************')
		return mingling
	except:
		pass

def add_one(one_name,one_name_num):
	one_per = {'name':'','num':''}
	get_namelist()
	if one_name in nameList:
		print('您输入的用户已存在,仍将继续保存')
	one_per['name'] = one_name
	one_per['num'] = one_name_num
	txl.append(one_per)
	print('您新增的姓名为：%s号码为%s已成功添加'%(one_name,one_name_num))
	time.sleep(2)

def del_one(one_name):
	get_namelist()
	if not one_name in nameList:
		print('您输入的名字，不在通讯录中，您可以选择选项*2*新增至通讯录中')
	else:
		for i in txl:
			if one_name == i['name']:
				txl.remove(i)
				print('删除成功，自动返回主菜单')
def check_one(one_name):
	get_namelist()
	if not one_name in nameList:
		print('您输入的名字，不在通讯录中，您可以选择选项*2*新增至通讯录中')
	else:
		for i in txl:
			if one_name == i['name']:
				print('您所查的姓名为%s的号码为%s'%(one_name,i['num']))
		

def get_user_name():
	get_user_name = input('请输入联系人的名字：')
	return get_user_name
def get_user_num():
 	get_user_num = input('请输入联系人号码：')
 	return get_user_num
	#将用户输入的数据组成列表追加到通讯录中

def prt_txl():	#打印通讯录
	print('='*30)
	#sum_txl = len(txl) #显示联系人总数
	#print（'联系人总数：%d'%sum_txl)
	print(left+'姓名: 号码')
	for i in txl:
		print(' '*5+i['name'],i['num'])
	print('='*30)

# def I_to_file(txl):#从文件中导入数据到通讯录表
# 	file_path = input('请输入文件所在目录的完整路径：')
# 	with open(file_path,'r') as f:
# 		txl=list(f.read())
# 	return txl

def O_to_file(txl):#从通讯录导出数据到文件中
	file_path = input('请输入文件要导出目录的完整路径：')
	file_path2 = file_path + "\list.txt"
	with open(file_path2,'w+') as f:
		f.write(str(txl))
	print('导出成功，返回主菜单')
	
def prt_menu():  #定义打印主界面菜单函数
	print('欢迎使用本通讯录管理系统(列表套字典)')
	time.sleep(1)
	print("-"*30),
	print('anthor: yu    date:20170808')
	print("-"*30),
	print(left+'选项 项目')
	print(left+'1.显示最新通讯录')
	print(left+'2.增加新的联系人')
	print(left+'3.修改联系人信息')
	print(left+'4.删除联系人信息')
	print(left+'5.查找联系人信息')
	print(left+'6.导出导入')
	print(left+'7.查看帮助')
	print(left+'8.退出本系统')
	print('~'*30),
	print('~'*30)

txl2 ={'李':'18734580623',
		'y44en':'18792121794',
		'张三':'18792322794'
		}
while True:
	print('\n'*10),
	prt_menu()
	mingling=get_mingli()
	if mingling==1:#打印
		prt_txl()
	elif mingling==2:#新增
		add_one(get_user_name(),get_user_num())
	elif mingling==3:#修改
		print('你可以通过删除后新增达到目的')
	elif mingling==4:#删除功能
		del_one(get_user_name())
	elif mingling==5:#通过姓名查找号码功能
		check_one(get_user_name())
	elif mingling==6:#导入导出
		print('''
			请选择导入或者导出到文件：，
			导入数据：1
			导出数据：2
			返回主菜单：3	
			''')
		mingling3=get_mingli()
		if mingling3==1:
			I_to_file()
		elif mingling3==2:
			O_to_file()
		elif mingling3==3:
			pass
		else:
			print('您输入的命令有误，将返回主菜单')
	elif mingling==7:
		print('按数字进入下级菜单操作，可以实现通讯录增删')		
	elif mingling==8:
		print('''#####警告#####
			请确认导出到文件后再退出，否则输入的数据会丢失！
			确认不导出退出：1
			取消返回主菜单：2	
			''')
		mingling2=get_mingli()
		if mingling2==1:
			print('感谢您使用本系统，欢迎您再次使用')
			time.sleep(0)
			break
	else:
		print('您输入的命令有误，请重新输入！！！')
		
