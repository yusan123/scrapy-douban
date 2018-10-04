#
#打印指定数字一下的斐波那契数列结论用yield Z好像要快一些
''
0,1,1,2,3,5,8,13,21
''
import time

def ber(num):
	ls = [0,1]
	while num>ls[-1]:
		newnum = ls[-1] + ls[-2]
		ls.append(newnum)
	return ls[:-1]


def febir(num):
	x,y = 0,1
	while x <num:
		yield x
		x,y = y,x+y

time1 = time.time()
for i in ber(100000000000000):
	print(i)
one = (time.time()-time1)


time2 = time.time()
for i in febir(100000000000000):
	print(i)
two =time.time()-time2

print((one-two)/two)
