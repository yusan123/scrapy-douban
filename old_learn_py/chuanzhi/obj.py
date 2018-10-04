class Car:
	"""docstring for Car"""
	def __init__(self, name='BYD',size='big',color='red'):
		#super(Car, self).__init__()
		self.name = name
		self.size = size
		self.color = color
		#self.maxsudu = maxsudu
	def __prtCar(self):
		print("This car's name is %s ,it is %s,and it is %s "\
			%(self.name,self.size,self.color))
	def test(self):
			self.__prtCar()	
# class Car2(Car):
# 	def __init__(self,maxsudu=100):
# 		Car.__init__(self, name='BYD',size='big',color='red')
# 		self.maxsudu = maxsudu
# 	def prtCar(self):
# 		print("This car's name is %s ,it is %s,and it is %s,it's sudu is "\
# 			%(self.name,self.size,self.color,self.maxsudu))
myCar1 = Car('benchi','small','blue')
myCar2 = Car()
myCar1.test()
myCar2.test()
print(myCar1.name)
print(myCar2.name)
print(myCar1.size)
print(myCar2.size)

#myCar2.prtCar()
		