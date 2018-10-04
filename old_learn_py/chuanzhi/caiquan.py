from random import randint

print('''
		=============================================
		Welcome to my first game : cai quan quan

		anthor : Yu Sen   Date : 20170806

		!mei you zhong wen shu ru fa zhi you zheyang
		=============================================

		''')
gametime = 5
while True:
	
	try:
	#player selet
		print('ni hai you %d ci ji hui'%gametime)
		player = int(input('please selet shitou(0)  jiandao(1)  bu(2):'))
	
		
		#computer selet
		computer = randint(0,2)

		#rule
		shitoujiandaobu = {0:'shitou',1:'jiandao',2:'bu'}

		#
		if not ((player == 0) or (player == 1) or (player == 2)):
			print('ni de shu ru you wu ,qing xuan ze |num: 0 or 1 or 2')
		else:
			if player == computer:  #shuzi xiangdeng kending pingju
				print('computer chose :'),shitoujiandaobu[computer]
				print('you chose:'),shitoujiandaobu[player]
				print('pingju,zai lai')
			else:
				if player - computer == -1 or player - computer == 2:
					#print('dian nao xuanze%d,ni shu le'%computer)	
					print('computer chose :'),shitoujiandaobu[computer]
					print('you chose:'),shitoujiandaobu[player]
					print('*')*20
					print('***gong xi ni ying le,ni hai you %s ci jihuimeiyong ***'%gametime)
					break
				else:
					#print('dian nao xuanze%d,ni ying le '%computer)
					print('computer chose: '),shitoujiandaobu[computer]
					print('you chose: '),shitoujiandaobu[player]
					print('ni shu le,zai lai')	
		
	except:
		print('ni de shu ru you wu ,qing xuan ze |num: 0 or 1 or 2')
	gametime-=1
	if gametime == 0:
			print('ni de ci shu yong wan ,mei you zhan sheng dian nao')
			break
	print("")
	print('----------------------------------------------------')
