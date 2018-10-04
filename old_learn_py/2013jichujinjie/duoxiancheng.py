import time
import threading

def test():
	print('1')
	time.sleep(1)
	print('1')
	

def test2():
	print('2')
	time.sleep(4)
	print('2')
	

firsttime = time.time()
for i in range(20):	
	test()
# test2()
print(time.time()-firsttime)


secondtime = time.time()
thrs = []
for i in range(10):
	i = threading.Thread(target = test)
	i.start()
	thrs.append(i)
for thr in thrs:
	thr.join()
#t2 = threading.Thread(target = test2)
# t1.start()
# t2.start()
# t1.join()
# t2.join()
print(time.time()-secondtime)