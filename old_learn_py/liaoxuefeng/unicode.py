#encoding:'utf-8'
def menu():
	print('1.汉字转数字')
	print('2.数字转汉字')
	print('3.退出')
def getorder():
	num = int(input('请输入你需要的功能指令：'))
	return num

def ch2Nnm():
	ls = []
	ch = input('请输入你要转换的中文内容：')
	for i in ch:
		ls.append(str(ord(i)-1))
	print(''.join(ls))
def num2Ch():
	ls = []
	num = input('请输入你要转换的数字内容：')
	for i in range(0,len(num),5):
		ls.append(chr(int(num[i:i+5])+1))
	print(''.join(ls))


while 1:
	menu()
	num = getorder()
	if num == 1:
		ch2Nnm()
	elif num == 2:
		num2Ch()
	elif num == 3:
		break
	else:
		print('输入的指令有误重新输入')

	