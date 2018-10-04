#coding=utf-8
#1.用主要用列表的方法存储数据，实现了通讯录的基本功能，除过读写其他没有问题
#2.改了一天终于没有明显问题,基本的增删查功能都实现了
#3.还是用字典存数据方法比较方便

import time 
lists=[['yus', '111111'], ['lijuan', '22222'],['pppp','23423423']]
# def clearpingmu():
# 	print('/n'*50)

def get_mingli():	#获取用户输入的指令
	try:
		mingling = int(input('请输入你需要的功能代码：'))
		print('********************************')
		return mingling
	except:
		pass
def del_one(one_name):
	global lists
	dic=dict(lists)
	if not one_name in dic:
		print('您输入的名字，不在通讯录中，您可以选择选项*2*新增至通讯录中')
	else:
		dic.pop(one_name)
		print('删除成功，自动返回主菜单')
		lists=[]
		for key in dic.keys():
			list1 = [key,dic[key]]
			lists.append(list1)

def check_one(one_name):#查找一个
	dic=dict(lists)
	if not one_name in dic:
		print('您输入的名字，不在通讯录中，您可以选择选项*2*新增至通讯录中')
	else:
		print('您所查的姓名为%s的号码为%s'%(one_name,dic[one_name]))

def get_user_name():
	get_user_name = input('请输入联系人的名字：')
	return get_user_name
def get_user_num():
 	get_user_num = input('请输入联系人号码：')
 	return get_user_num

	#将用户输入的数据组成列表追加到通讯录中
def add_one(one_name,one_name_num):
	dic=dict(lists)
	if one_name in dic:
		print('您输入的名字，已在通讯录中，暂不能添加，将返回主菜单')
	else:
		one_per = []
		one_per.append(one_name)
		one_per.append(one_name_num)
		lists.append(one_per)
		print('新增的名字为：%s已成功'%one_name)

def prt_lists():	#打印通讯录
	print('='*30)
	print('姓名: 号码')
	for one_per in lists:
			print(one_per[0]+":"+one_per[1])
	print('='*30),

def I_to_file(lists):#从文件中导入数据到通讯录表
	try:
		file_path = input('请输入文件所在目录的完整路径：')
		with open(file_path,'r') as f:
			lists=list(f.read())
		return lists
	except:
		print('您输入的路径有误，请确认后重新操作')

def O_to_file(lists):#从通讯录导出数据到文件中
	try:
		file_path = input('请输入文件要导出目录的完整路径：')
		file_path2 = file_path + "\list.txt"
		with open(file_path2,'w+') as f:
			f.write(str(lists))
		print('导出成功，返回主菜单')
	except:
		print('您输入的路径有误，请确认后重新操作')

def prt_menu():  #定义打印主界面菜单函数
	print('欢迎使用本通讯录管理系统（列表套列表版）')
	time.sleep(1)
	print("-"*30),
	print('anthor: yu    date:20170808')
	print("-"*30),
	print('选项'            '项目')
	print('1.'              '显示最新通讯录')
	print('2.'              '增加新的联系人')
	print('3.'              '修改联系人信息')
	print('4.'              '删除联系人信息')
	print('5.'              '查找联系人信息')
	print('6.'              '导出导入')
	print('7.'              '查看帮助')
	print('8.'              '退出本系统')
	print('~'*30),
	print('~'*30)

while True:
	print('\n'*10),
	prt_menu()
	mingling=get_mingli()
	if mingling==1:
		prt_lists()
		time.sleep(3)
	elif mingling==2:
		add_one(get_user_name(),get_user_num())
	elif mingling==3:
		print('功能等待完善，你可以通过删除后新增达到目的')	
	elif mingling==4:
		del_one(get_user_name())
		time.sleep(2)
	elif mingling==5:#通过姓名查找号码功能
		check_one(get_user_name())
		time.sleep(2)
	elif mingling==6:
		print('''
			请选择导入或者导出到文件：，
			导入数据：1
			导出数据：2
			返回主菜单：3	
			''')
		mingling3=get_mingli()
		if mingling3==1:
			#I_to_file(lists)
			print('暂时不能使用')
		elif mingling3==2:
			O_to_file(lists)
			time.sleep(2)
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
			time.sleep(1)
			break
	else:
		print('您输入的命令有误，请重新输入！！！')
		
