#-*-coding:utf-8-*-
from random import randint
gametime = 3
print('''
===========================================
欢迎来到我的第一个游戏 : 猜拳
作者 : YS   Date : 20170806
温馨提示：
    你有 %d 次机会战胜电脑，输错也会浪费机会。
    祝你好运！！！！！！！
===========================================

		'''%gametime)
while True:
    print('你还有 %d 次机会'%gametime)
    gametime-=1
    try:
        #player selet
        player = int(input('请选择输入数字： 石头(0)  剪刀(1)  布(2):'))
        #computer selet
        computer = randint(0,2)
        #rule
        rule = {0:'石头',1:'剪刀',2:'布'}
        if not ((player == 0) or (player == 1) or (player == 2)):
            print('你输入数字有误，请输入数字: 0 or 1 or 2')
        else:
            if player == computer:  #shuzi xiangdeng kending pingju
                print('电脑出的是:   %s '%rule[computer])
                print('你出的是:   %s'%rule[player])
                print('平局，再来！')
            else:
                if (player - computer == -1) or (player - computer) == 2:
                    print('电脑出的是:   %s '%rule[computer])
                    print('你出的是:   %s'%rule[player])
                   # print('*')*20
                    print('*恭喜你！战胜了电脑！你还有 %d 次机会没有使用！ *'%gametime)
                    break
                else:
                    print('电脑出的是:   %s '%rule[computer])
                    print('你出的是:   %s'%rule[player])
                    print('你输了，再来！')		
    except:
        print('你的输入不是数字，请输入数字: 0 or 1 or 2')
    if gametime == 0:
        print('你的剩余游戏次数已为0,没有战胜电脑\
              \n请重新开始游戏，祝你下次好运！')
        break
    print("")
    print('----------------------------------------------------')
enter = input()
