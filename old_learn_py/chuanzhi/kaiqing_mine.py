#coding=utf-8
#功能描述：
#			小明拿着一把枪打老王，枪有弹夹，弹夹李有子弹，
#子弹有杀伤力，每次开枪老王会掉子弹杀伤力的血，掉到0为死


#人
class Ren:
	def __init__(self,name):
		self.name = name
		self.__life = 100

	def maiQiang(self,qiang):
		self.qiang = qiang
		print('%s买了一把%s'%(self.name,qiang.name))

	def yanzidan(self,danjia,zidan):
		danjia.zhuangzidan(zidan)

	def zhuangdanjia(self,danjia):
		self.qiang.danjia = danjia
		print('%s已经装好弹夹,弹夹里有子弹数%d'%\
(self.qiang.name,len(self.qiang.danjia.zidanliebiao)))

	def kaiqiang(self,mubiao):
		print('%s向%s开枪'%(self.name,mubiao.name))
		self.qiang.fashe(mubiao)
		#mubiao.diaoxue(self.qiang)
 		#print('%s被%s打中，掉血%d,当前生命值为：%d'%(mubiao.name,self.qiang.name,self.qiang.danjia.chuzidan(),mubiao.__life))
		
	def diaoxue(self,shashangli):
		if self.__life>shashangli:
			self.__life-=shashangli
		else:
			self.__life =0
		print('%s掉血%d,当前生命值为%d'%(self.name,shashangli,self.__life))
		


class Qiang:
	def __init__(self,name):
		self.name = name
	def danjia(self,danjia):
		self.danjia = danjia

	def fashe(self,mubiao):
		shashangli = self.danjia.chuzidan()
		mubiao.diaoxue(shashangli)



#弹夹
class Danjia:
	def __init__(self,rongliang):
		self.rongliang = rongliang
		self.zidanliebiao = []

	def zhuangzidan(self,zidan):
		self.zidanliebiao.append(zidan)
		#print('新加入的子弹的：%d'%zidan.shashangli)
		print('向弹夹填入子弹+1杀伤力为:%d,当前子弹数\
为：%d'%(zidan.shashangli,len(self.zidanliebiao)))

	def chuzidan(self):
		if len(self.zidanliebiao)>0:
			zidan = self.zidanliebiao[-1]
			shashangli = zidan.shashangli
			self.zidanliebiao.pop()
			print('子弹-1,当前子弹数为：%d'%len(self.zidanliebiao))
		else:
			print('弹夹没有子弹了，请装弹')
			shashangli = 0
		return shashangli

	

		

#子弹
class Zidan:
	def __init__(self,shashangli):
		self.shashangli = shashangli
	
		

#创建开枪的小明 
xiaoming = Ren('小明')
#创建老王
laowang = Ren('老王')

#创建了一把名叫ak47的枪
ak47 = Qiang('ak47')

#买枪
xiaoming.maiQiang(ak47)

#创建一个最大100发的弹夹
danjia =Danjia(100)


#创建子弹
zidan = Zidan(10)
zidan2 = Zidan(50)
zidan3 = Zidan(80)
#zidan4 = Zidan(20)

#小明给弹夹里装子弹
xiaoming.yanzidan(danjia,zidan)
xiaoming.yanzidan(danjia,zidan2)
xiaoming.yanzidan(danjia,zidan3)
#xiaoming.yanzidan(danjia,zidan4)

#小明将装好子弹的弹夹装上枪
xiaoming.zhuangdanjia(danjia)

#小明开枪
xiaoming.kaiqiang(laowang)
xiaoming.kaiqiang(laowang)
xiaoming.kaiqiang(laowang)
xiaoming.kaiqiang(laowang)

